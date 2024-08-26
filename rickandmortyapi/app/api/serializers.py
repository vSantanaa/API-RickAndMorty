from rest_framework import serializers
from models import RickAndMorty

class RickAndMortySerializer(serializers.ModelSerializer):
    class Meta:
        model= RickAndMorty
        fields = ['id','nome','genero','status','especie', 'origem', 'localizacao', '']