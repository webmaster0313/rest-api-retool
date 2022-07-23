from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pokedex.api import views

urlpatterns = [
    path('pokemon/', views.PokemonList.as_view(), name='pokemon-list'),
    path('pokemon/<int:pk>/', views.PokemonDetail.as_view(), name='pokemon-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
