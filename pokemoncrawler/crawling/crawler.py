from pokemoncrawler.helpers.poke_api import get_pokemons, get_pokemon
from pokemoncrawler.models import Pokemon, Ability, Stat


class Crawler():
    
    def crawl_pokemon(self, pokemon):
        pokemon_results = get_pokemon(pokemon)
        
        obj, created = Pokemon.objects.get_or_create(name=pokemon_results['name'])
        
        pokemon_abilities = []
        for pokemon_results_ability in pokemon_results['abilities']:
            pokemon_abilities.append(Ability.objects.get(name=pokemon_results_ability['ability']['name']))
        obj.abilities.set(pokemon_abilities)
        obj.save()

        pokemon_stats = []
        for pokemon_results_stat in pokemon_results['stats']:
            pokemon_stats.append(Stat.objects.get(name=pokemon_results_stat['stat']['name']))
        obj.stats.set(pokemon_stats)
        obj.save()
