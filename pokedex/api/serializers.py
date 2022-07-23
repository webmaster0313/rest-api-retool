from rest_framework import serializers
from pokedex.api.models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['pk','name','nickname','date_added','pokeapi_url']
        read_only_fields = ['pk','date_added']
