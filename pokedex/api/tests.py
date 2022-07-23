from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pokedex.api.models import Pokemon

class AnimalTestCase(APITestCase):

    def setUp(self):
        Pokemon.objects.create(name='Charizard', nickname='Chaz', pokeapi_url='http://whatever.com')
        Pokemon.objects.create(name='Bulbasaur', nickname='Bulba', pokeapi_url='http://bulbasaur.com')

    def test_get_list_of_pokemon(self):

        url = reverse('pokemon-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.status_code, 200)

        first = response.data[0]
        second = response.data[0]

        self.assertTrue(first['name'] in ['Charizard','Bulbasaur'])
        self.assertTrue(second['name'] in ['Charizard','Bulbasaur'])
        self.assertTrue(first['pokeapi_url'] in ['http://whatever.com','http://bulbasaur.com'])
        self.assertTrue(second['pokeapi_url'] in ['http://whatever.com','http://bulbasaur.com'])

    def test_add_pokemon(self):

        url = reverse('pokemon-list')
        data = {
            'name': 'Wartortle',
            'nickname': 'Warhoss',
            'pokeapi_url': 'http://wartortle.com'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        wartortle = Pokemon.objects.get(name='Wartortle')
        self.assertEqual(wartortle.pokeapi_url, 'http://wartortle.com')

    def test_update_pokemon(self):

        bulbasaur = Pokemon.objects.get(name='Bulbasaur')

        url = reverse('pokemon-detail', args=[bulbasaur.pk])
        data = {
            'pk': bulbasaur.pk,
            'name': 'Wartortle',
            'nickname': 'Warhoss',
            'pokeapi_url': 'http://wartortle.com'
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)

        wartortle = Pokemon.objects.get(name='Wartortle')
        self.assertEqual(wartortle.pokeapi_url, 'http://wartortle.com')
        self.assertEqual(wartortle.nickname, 'Warhoss')

    def test_remove_pokemon(self):

        bulbasaur = Pokemon.objects.get(name='Bulbasaur')

        url = reverse('pokemon-detail', args=[bulbasaur.pk])

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        charizard = Pokemon.objects.get(name='Charizard')
        self.assertEqual(Pokemon.objects.all().count(), 1)
