from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger

from restaurant.models import Restaurant

logger = get_task_logger(__name__)


@shared_task(name='food.add_search_score')
def add_search_score(res_id: int) -> object:
    sleep(5)
    restaurant: Restaurant = Restaurant.objects.get(pk=res_id)
    restaurant.hit_score = restaurant.hit_score + 0.1
    restaurant.save()
    logger.info('restaurant hit score updated')
    return

