from django.test import TestCase
from pokemoncrawler.tasks import crawl_poke_task
from pokemoncrawler.models import Pokemon


# Create your tests here.
class PokemonModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pokemon.objects.create(name="test_pokemon")
        Pokemon.objects.create(name="test_pokemon_2")

    def test_create_pokemon(self):
        pokemons = Pokemon.objects.all()
        self.assertEqual(len(pokemons), 2)


class CrawlPokemonTestCase(TestCase):
    def test_crawl_one_pokemon(self):
        crawl_poke_task.s("ditto").apply()
        ditto_pokemon = Pokemon.objects.get(name="ditto")
        self.assertEqual(ditto_pokemon.name, "ditto")