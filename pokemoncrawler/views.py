from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from pokemoncrawler.crawling.crawling_service import start_crawler
from pokemoncrawler.models import Pokemon

# Create your views here.
def start_crawling(request):
    start_crawler()
    return HttpResponse("Started Crawling")

def get_pokemons(request):
    pokemons = Pokemon.objects.all()
    poke_list = serializers.serialize('json', pokemons)
    return HttpResponse(poke_list, content_type="text/json-comment-filtered")
