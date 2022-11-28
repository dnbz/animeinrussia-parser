#!/usr/bin/env python3
import locale

from .models import Show
from .tg import send_photo as tg_send_photo
from animeinrussia.settings import TELEGRAM_CHAT_ID
from datetime import datetime
from string import Template

def time_now():
    return datetime.now().replace(microsecond=0)

def send_tg_message(show: Show):
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

    date = show.pub_date.strftime("%-d %B %Y года")

    template = Template(
    """\
    Анимe «$title_ru» ($title_orig) в прокате с $date\n\n$description
    """
    )

    msg = template.substitute(
        {
            "title_ru": show.title_ru,
            "title_orig": show.title_orig,
            "description": show.description,
            "date": date,
        }
    )

    result = tg_send_photo(TELEGRAM_CHAT_ID, photo_url=show.image_url, msg=msg)

    if result:
        show.sent_at = time_now()
        show.save()
        return result
    else:
        return None
