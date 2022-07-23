# retool-pokedex

REST API to support list, create, and delete operations for a Pokemon list for a simple Retool project.

## Endpoints

`pokemon/`
- `GET` list of Pokemon in the database
- Example response:
```
{
  'pk': '5',
  'name': 'Wartortle',
  'nickname': 'Warhoss',
  'pokeapi_url': 'http://wartorle.com',
  'date_added': '2020-02-09'
}
```

`pokemon/`
- `POST` create new Pokemon in the database
- Example `POST`:
```
{
  'name': 'Wartortle',
  'nickname': 'Warhoss',
  'pokeapi_url': 'http://wartorle.com',
  'date_added': '2020-02-09'
}
```

`pokemon/{pk}`: `DELETE` Delete single Pokemon from the database

`pokemon/{pk}`: `PUT` Update single Pokemon in the database

## Testing

All endpoint functionality (list, create, delete) is covered.

`python manage.py test`

## Running locally

The app is configured to run on Heroku.
To run locally, create a `local_settings.py` file and drop into the `api/` directory.

```
#local_settings.py

DEBUG = True

SECRET_KEY = YOUR_SECRET_KEY
```
