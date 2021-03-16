from django.db import models


class Pokemon(models.Model):
    """Покемон."""

    title = models.CharField(max_length=200, verbose_name="имя покемона")
    picture = models.ImageField(
        upload_to="pokemon_pic", null=True, blank=True, verbose_name="изображение"
    )

    description = models.CharField(max_length=2000, blank=True, verbose_name="описание")

    title_en = models.CharField(
        max_length=200, blank=True, verbose_name="английское имя покемона"
    )
    title_jp = models.CharField(
        max_length=200, blank=True, verbose_name="японское имя покемона"
    )

    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="next_evolution",
        verbose_name="из кого эволюционирует",
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    """Покемон на карте."""

    latitude = models.FloatField(verbose_name="широта")
    longitude = models.FloatField(verbose_name="долгота")

    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="имя покемона"
    )

    appeared_at = models.DateField(null=True, blank=True, verbose_name="появился")
    disappeared_at = models.DateField(null=True, blank=True, verbose_name="исчез")

    level = models.IntegerField(null=True, blank=True, verbose_name="уровень")
    health = models.IntegerField(null=True, blank=True, verbose_name="жизнь")
    strength = models.IntegerField(null=True, blank=True, verbose_name="сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name="защита")
    stamina = models.IntegerField(null=True, blank=True, verbose_name="выносливость")

    def __str__(self):
        return self.pokemon.title
