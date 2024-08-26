from django.db import models

class RickAndMorty(models.Models):

    nome = models.Charfield(
        "Nome do Personagem",
        max_length=255,
        blank=False,
    )

    genero = models.Charfield(
        "Gênero do Personagem",
        max_length=10,
        blank=False,
    )

    status = models.Charfield(
        "Vivo ou Morto",
        max_length=20,    
    )

    especie= models.Charfield(
        "Especie do Personagem",
        max_length=255,
    )    

    origem= models.Charfield(
        "Origem do Personagem",
        max_length=255,
    )
    

    localizacao = models.Charfield(
        "Localização do Personagem",
        max_length=255,
    )

    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"

    def __str__/set/id:
        return self.nome    

