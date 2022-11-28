import json

from celery import shared_task
from .models import Show
from .show import send_tg_message
from animeinrussia.settings import TELEGRAM_CHAT_ID
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def time_now():
    return datetime.datetime.now().replace(microsecond=0)

@shared_task
def debug_task():
    show = Show.objects.filter(
        sent_at=None
    ).order_by('pub_date').first()

    if not show:
        return

    logger.info(f"Trying to send message for show with id {show.id}")
    result = send_tg_message(show)
    logger.info(json.dumps(result, indent=4, ensure_ascii=False))

    logger.info(f"{show.source_url}")
