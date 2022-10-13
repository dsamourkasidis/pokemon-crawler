import requests
from django.core.management.base import BaseCommand
from pokemoncrawler.models import Ability, Stat
from pokemoncrawler.constants import POKE_API_BASE_URL, STATS_ENDPOINT, ABILITIES_ENDPOINT
from pokemoncrawler.helpers.poke_api import get_abilities, get_stats

def seed_abilities():
  abilities = get_abilities()
  for ability in abilities:
    Ability.objects.get_or_create(name=ability['name'])
  
def seed_stats():
  stats = get_stats()
  for stat in stats:
    Stat.objects.get_or_create(name=stat['name'])
    

class Command(BaseCommand):
  def handle(self, *args, **options):
    seed_abilities()
    seed_stats()
    print("abilities and stats seeded!")

