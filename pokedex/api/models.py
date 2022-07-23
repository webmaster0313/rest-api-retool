from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    pokeapi_url = models.URLField()

    class Meta:
        unique_together = ['name', 'nickname']
