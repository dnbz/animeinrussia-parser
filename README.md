# Парсер для сайта animeinrussia.ru
Берутся данные с сайта и отправляются сообщения в телеграм-канал через бота.

Парсер написан с помощью scrapy, пишет в postgres.

Django брал для [django-celery-beat](https://github.com/celery/django-celery-beat) и для ORM. Оказалось перебором, можно было и без него обойтись

## Конфигурация
Создать в каждом проекте по примеру .env.example

## Запуск сервисов
```sh
kubectl apply -f kubernetes/
```

## Запуск парсера
```sh
cd animeinrussia_parser
poetry install
poetry shell

scrapy crawl air-spider
```

## Запуск celery
```sh
cd animeinrussia_api
poetry install
poetry shell

celery -A animeinrussia worker --beat --loglevel=info
```
