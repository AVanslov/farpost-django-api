![example event parameter](https://github.com/avanslov/farpost-django-api/actions/workflows/main.yml/badge.svg?event=push)

# Описание

API-сервис для получения данных о первых 10 объявлениях по [ссылке](https://www.farpost.ru/vladivostok/service/construction/guard/+/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/) с сервиса farpost.ru


# Cтек
![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/-Django_REST_FRAMEWORK-black?style=for-the-badge&logo=Django)
![Scrapy](https://img.shields.io/badge/-Scrapy-black?style=for-the-badge&logo=Scrapy)
![ReDoc](https://img.shields.io/badge/-ReDoc-black?style=for-the-badge&logo=ReDoc)
![Pytest](https://img.shields.io/badge/-Pytest-black?style=for-the-badge&logo=Pytest)


# Установка и запуск

***Клонировать репозиторий и перейти в него в командной строке:***

```
git clone git@github.com:your_username_in_github/farpost-django-api.git
```

***Cоздать и активировать виртуальное окружение:***
```

Для Windows:
python -m venv env
source venv/Script/activate

Для Linux/MacOS:
python3 -m venv env
source venv/bin/activate
```
***Установить зависимости из файла requirements.txt:***

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

***Как заполнить .env:***

В случае запуска в режиме DEBUG=False корневой папке проекта создайте файл .env и скопируйте в него код с поля ниже.

```
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
```

**Запуск проекта**

Для запуска проекта поочередно выполните команды из листинга

```
sudo docker compose stop && sudo docker compose up --build

# миграции и запуск парсера выполняется автоматически в Dockerfile

sudo docker compose exec backend python manage.py collectstatic

sudo docker compose exec backend cp -r /app/farpost/collected_static/. /backend_static/static/

sudo docker compose exec backend python manage.py loaddata ../data/final_data_farpost_authors.json

sudo docker compose exec backend python manage.py loaddata ../data/final_data_farpost_adds.json
```

## Как реализован сбор данных

С помощью фреймворка для парсинга данных Scrapy собираются данные. Для этого последовательно выполняются две операции.

**Сбор данных непосредственно со страницы поиска:**
- количестве просмотрах,
- позиции в списке выдачи,
- названии

**С помощью CrawlScrapy во втором скрипте паук заходит на страницу каждого объявления:**
- для получения информации об авторе

Далее данные конвертируются и склеиваются в единый JSON для последующего импорта в БД.

## API

### Документация к API

Оформленная документация к API доступна после запуска приложения по адресу:
http://localhost:8000/swagger/

#### Авторизация

Авторизация реализована с помощью Djoser.
В настройках проекта задан срок жизни токена 1 день, установлен лимит запросов в сутки.

Регистрация и авторизация состоит из двух шагов.

POST запрос с логином и паролем

```
POST http://localhost:8000/auth/users/
Content-Type: application/json

{
    "username": "test",
    "password":  "lsjafw39hfd"
}
```
POST запрос для получения JWT токена для последющей передачи в каждом запросе

```
POST http://localhost:8000/auth/jwt/create/
Content-Type: application/json

{
    "username": "test",
    "password":  "lsjafw39hfd"
}
```
Токен следует передавать следующим образом:

```
GET http://localhost:8000/api/adds/
Content-Type: application/json
Authorization: Bearer <токен>
```



### Как протестировать API

Запросы для тестирования доступны в корневой папке проекта в файле requests.http

**В данном API есть возможность выполнить следующие запросы:**

- Получение всех объявлений, при этом на уровне проекта настроена пагинация по 5 объявлений на страницу.

- Получение конкретного объявления по его ID номеру, который указан на [сайте источнике](https://www.farpost.ru/vladivostok/service/construction/guard/+/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/).

*ID объявления храниться в БД в поле add_id модели Add.*

**Примеры запросов**
```
###
GET http://localhost:8000/api/adds/
Content-Type: application/json
Authorization: Bearer <токен>
```
```
###
GET http://localhost:8000/api/adds/<add_id>/
Content-Type: application/json
Authorization: Bearer <токен>
```


# Автор
## Александр Бучельников

[![Personal-Website](https://img.shields.io/badge/-Personal_website-black?style=for-the-badge&logo=)](https://buchelnikov.ddns.net/)

## Contact me

[![Telegram](https://img.shields.io/badge/-Telegram-black?style=for-the-badge&logo=Telegram)](https://t.me/aleksandr_buchelnikov)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black?style=for-the-badge&logo=LinkedIn)](https://www.linkedin.com/in/aleksandr-buchelnikov/)
[![E-mail](https://img.shields.io/badge/-E_mail-black?style=for-the-badge&logo=Gmail)](mailto:al.buchelnikov@gmail.com)