# Generated by Django 3.1.7 on 2021-03-15 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0007_pokemon_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="title_en",
            field=models.CharField(default="Title en", max_length=200),
        ),
        migrations.AddField(
            model_name="pokemon",
            name="title_jp",
            field=models.CharField(default="Title jp", max_length=200),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="description",
            field=models.CharField(max_length=2000),
        ),
    ]
