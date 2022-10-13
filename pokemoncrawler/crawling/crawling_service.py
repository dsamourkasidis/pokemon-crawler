from pokemoncrawler.helpers.poke_api import get_pokemons, get_pokemon
from pokemoncrawler.models import Pokemon, Ability, Stat
from pokemoncrawler.tasks import crawl_poke_task


def start_crawler():
    pokemons = get_pokemons()
    pokemon_names = [p['name'] for p in pokemons]
    crawl_poke_task.chunks(zip(pokemon_names), 50)()