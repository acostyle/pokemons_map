# Generated by Django 3.1.7 on 2021-03-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0004_pokemonentity_pokemon"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonentity",
            name="appeared_at",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="pokemonentity",
            name="disappeared_at",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="pokemon",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="pokemon_entities.pokemon",
            ),
            preserve_default=False,
        ),
    ]
