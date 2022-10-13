import requests
from pokemoncrawler.constants import POKE_API_BASE_URL, STATS_ENDPOINT, ABILITIES_ENDPOINT, POKEMONS_ENDPOINT, POKEMON_ENDPOINT


def get_abilities():
    r = requests.get(POKE_API_BASE_URL + ABILITIES_ENDPOINT)
    abilities = r.json()
    return abilities['results']

def get_stats():
    r = requests.get(POKE_API_BASE_URL + STATS_ENDPOINT)
    stats = r.json()
    return stats['results']
        
def get_pokemons():
    r = requests.get(POKE_API_BASE_URL + POKEMONS_ENDPOINT)
    pokemons = r.json()
    return pokemons['results']

def get_pokemon(pokemon_id_or_name):
    r = requests.get(f'{POKE_API_BASE_URL}{POKEMON_ENDPOINT}{pokemon_id_or_name}')
    pokemon = r.json()
    return pokemon