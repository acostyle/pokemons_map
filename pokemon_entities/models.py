from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pokemon_pic', null=True, blank=True)

    description = models.CharField(max_length=2000, blank=True)

    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    appeared_at = models.DateField(null=True, blank=True)
    disappeared_at = models.DateField(null=True, blank=True)

    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True) 