#!/usr/bin/env python3
import requests
from animeinrussia.settings import TELEGRAM_BOT_TOKEN

def get_baseurl():
    token = TELEGRAM_BOT_TOKEN

    url = f"https://api.telegram.org/bot{token}"

    return url

def send_photo(chat_id: str, msg: str, photo_url: str):
    baseurl = get_baseurl()
    api_url = f"{baseurl}/sendPhoto"

    body = {
        "caption": msg,
        "photo": photo_url,
        "chat_id": chat_id,
        # "parse_mode": "markdown"
    }

    response = requests.post(api_url, data=body)

    return response.text

def send_message(chat_id: str, msg: str):
    baseurl = get_baseurl()
    api_url = f"{baseurl}/sendMessage"

    body = {
        "text": text,
        "chat_id": chat_id,
        # "parse_mode": "markdown"
    }

    response = requests.post(api_url, data=body)

    return response.json
