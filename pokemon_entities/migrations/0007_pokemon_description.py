# Generated by Django 3.1.7 on 2021-03-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0006_auto_20210315_2003"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="description",
            field=models.CharField(default="Default description", max_length=2000),
        ),
    ]
