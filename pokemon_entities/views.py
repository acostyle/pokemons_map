import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import PokemonEntity, Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # tooltip=name,  # disable tooltip because of folium encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        for pokemon_entity in pokemon_entities:
            add_pokemon(
                folium_map,
                pokemon_entity.latitude,
                pokemon_entity.longitude,
                request.build_absolute_uri(pokemon.picture.url),
            )

    pokemons_on_page = []
    for pokemon in Pokemon.objects.all():
        pokemons_on_page.append(
            {
                "pokemon_id": pokemon.id,
                "img_url": pokemon.picture.url if pokemon.picture else None,
                "title_ru": pokemon.title,
            }
        )

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    pokemons = Pokemon.objects.all()

    for pokemon in pokemons:
        if pokemon.id == int(pokemon_id):
            requested_pokemon = pokemon
            break
    else:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon__id=requested_pokemon.id)

    for pokemon_entity in pokemon_entities:
        pokemon_characteristics = {
            "title_ru": requested_pokemon.title,
            "title_en": requested_pokemon.title_en,
            "title_jp": requested_pokemon.title_jp,
            "img_url": request.build_absolute_uri(requested_pokemon.picture.url),
            "description": requested_pokemon.description,
        }
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon_characteristics["img_url"],
        )

    if pokemon.previous_evolution:
        pokemon_characteristics["previous_evolution"] = {
            "title_ru": pokemon.previous_evolution.title,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": request.build_absolute_uri(
                pokemon.previous_evolution.picture.url
            ),
        }

    next_evolution = pokemon.next_evolution.first()
    if next_evolution:
        pokemon_characteristics["next_evolution"] = {
            "title_ru": next_evolution.title,
            "pokemon_id": next_evolution.id,
            "img_url": request.build_absolute_uri(next_evolution.picture.url),
        }

    return render(
        request,
        "pokemon.html",
        context={"map": folium_map._repr_html_(), "pokemon": pokemon_characteristics},
    )
