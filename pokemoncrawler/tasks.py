from pokemoncrawler.crawling.crawler import Crawler
from celery import shared_task


@shared_task
def crawl_poke_task(pokemon_name):
    poke_crawler = Crawler()
    poke_crawler.crawl_pokemon(pokemon_name)
    