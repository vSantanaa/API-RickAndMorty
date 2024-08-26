from rest_framework import viewsets
from .serializers import RickAndMortySerializer, RickAndMorty
import requests
from rest_framework_response import Response

class RickAndMortyViewSet(viewsets.ModelViewSet):
    serializer_class = RickAndMortySerializer
    queryset = RickAndMorty.objects.all()

    def create(self, request):

        nome_personagem = request.data.get("nome", '')
        nome_codificado = quote(nome_personagem.lower())

        try:

            requisicao = requests.get("https://rickandmortyapi.com/api/character/?name={}=")
        except requests.RequestException as e:
            return Response({"aviso":f"Erro ao acessar a API externa:{e}"}) 

        json = requisicao.json()

        if"results" in json and len(json['results']) > 0:
            personagem = json['results'][0]
        else:
            return Response({"aviso":f"Personagem não encontrado"})

        nome = personagem.get("name",'')
        genero = personagem.get("gender", '')
        status = personagem.get("status",'')
        especie = personagem.get("species",'')
        origem = personagem.get("origin", {}.get("name",''))
        localizacao = personagem.get("location",{}.get("name",''))

        personagem_criado = (
            "nome": nome,
            "genero": genero,
            "status": status,
            "especie": especie,
            "origem": origem,
            "localizacao": localizao,
        )
        
        meuserializador = RickAndMortySerializer(data=personagem_criado)

        if meuserializador.is_valid():

            personagem_validation = RickAndMorty.objects.filter(nome=nome)
            personagem_existe = personagem_validation.exists()

            if personagem_existe:
                return Response({"aviso":"Personagem já existe"})

            meuserializador.save()
            return Response({"aviso":"Personagem criado com sucesso!"})

            else:
                return Response({"aviso":"Esse personagem não é válido"})

