# Generated by Django 3.0.3 on 2020-02-11 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_pokemon_pokeapi_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='nickname',
            field=models.CharField(default='Charizard', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='pokemon',
            unique_together={('name', 'nickname')},
        ),
    ]