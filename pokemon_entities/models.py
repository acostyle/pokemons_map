from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pokemon_pic', null=True, blank=True)


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)