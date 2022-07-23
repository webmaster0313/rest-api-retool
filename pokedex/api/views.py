from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pokedex.api.models import Pokemon
from pokedex.api.serializers import PokemonSerializer

class PokemonList(APIView):
    """
    List all pokemon, or create a new pokemon.
    """
    def get(self, request, format=None):
        pokemon = Pokemon.objects.all().order_by('-date_added')
        serializer = PokemonSerializer(pokemon, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonDetail(APIView):
    """
    Delete a pokemon instance.
    """
    def get_object(self, pk):
        try:
            return Pokemon.objects.get(pk=pk)
        except Pokemon.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        pokemon = self.get_object(pk)
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pokemon = self.get_object(pk)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
