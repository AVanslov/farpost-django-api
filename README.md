![example event parameter](https://github.com/avanslov/farpost-django-api/actions/workflows/main.yml/badge.svg?event=push)

# EN
# Description

**API service for getting data on the first 10 ads by [link](https://www.farpost.ru/vladivostok/service/construction/guard/+/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/ ) from the service farpost.ru**

The project is designed in such a way that it is easy to expand, test and put into operation.

All the work on the CI/CD pre-configuration has been completed.

The project is easy to run locally using docker-compose.

# Stack
![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/-Django_REST_FRAMEWORK-black?style=for-the-badge&logo=Django)
![Scrapy](https://img.shields.io/badge/-Scrapy-black?style=for-the-badge&logo=Scrapy)
![Nginx](https://img.shields.io/badge/-Nginx-black?style=for-the-badge&logo=Nginx)
![Docker](https://img.shields.io/badge/-Docker-black?style=for-the-badge&logo=Docker)
![Swager](https://img.shields.io/badge/-Swager-black?style=for-the-badge&logo=Swager)
![GitHub](https://img.shields.io/badge/-GitHub_Actions-black?style=for-the-badge&logo=GitHub)


# Installation and launch

***Clone the repository and go to it on the command line:***

```
git clone git@github.com:your_username_in_github/farpost-django-api.git
```

***Create and activate a virtual environment:***
```

For Windows:
python -m venv env
source venv/Script/activate

For Linux/macOS:
python3 -m venv env
source venv/bin/activate
```
***Install dependencies from a file requirements.txt:***

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

***How to fill in .env:***

If you run in DEBUG=False mode, create a .env file in the root folder of the project and copy the code from the field below into it.

```
POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
```

**Project launch**

To run the project, run the commands from the listing one at a time

```
sudo docker compose stop && sudo docker compose up --build
```

migrations and parser startup are performed automatically in Dockerfile

```
sudo docker compose exec backend python manage.py collectstatic

sudo docker compose exec backend cp -r /app/farpost/collected_static/. /backend_static/static/

sudo docker compose exec backend python manage.py loaddata ../data/final_data_farpost_authors.json

sudo docker compose exec backend python manage.py loaddata ../data/final_data_farpost_adds.json
```

## How data collection is implemented

Data is collected using the Scrapy data parsing framework. To do this, two operations are performed sequentially.

**Collecting data directly from the search page:**
- the number of views,
- positions in the issue list,
- the name

**Using CrawlScrapy in the second script, the spider enters the page of each ad:**
- to get information about the author

Next, the data is converted and glued into a single JSON for subsequent import into the database.

## API

### API Documentation

The completed API documentation is available after the application is launched at:
http://localhost:8000/swagger/

#### Authorization

Authorization is implemented using Djoser.
The token's lifetime is set to 1 day in the project settings, and the request limit per day is set.

Registration and authorization consists of two steps.

POST request with username and password

```
POST http://localhost:8000/auth/users/
Content-Type: application/json

{
"username": "test",
"password": "lsjafw39hfd"
}
```
POST a request to receive a JWT token for subsequent transmission in each request

```
POST http://localhost:8000/auth/jwt/create/
Content-Type: application/json

{
    "username": "test",
    "password":  "lsjafw39hfd"
}
```
The token should be transmitted as follows:

```
GET http://localhost:8000/api/adds/
Content-Type: application/json
Authorization: Bearer <token>
```

### How to test the API

Requests for testing are available in the root folder of the project in the requests.http file

**In this API, it is possible to make the following requests:**

- Receiving all ads, while pagination of 5 ads per page is configured at the project level.

- Receiving a specific ad by its ID number, which is indicated on the [website](https://www.farpost.ru/vladivostok/service/construction/guard/+/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/).

*The ad ID is stored in the database in the add_id field of the Add model.*

**Examples of requests**
```
###
GET http://localhost:8000/api/adds/
Content-Type: application/json
Authorization: Bearer <token>
```

```
###
GET http://localhost:8000/api/adds/<add_id>/
Content-Type: application/json
Authorization: Bearer <token>
```

### Development ideas

To work out the logic of the parser, now two queries can be combined into one script for generating JSON, and also add logic to exclude duplicates of the author's object in the database when importing fixtures.

Write tests, for example, on Pytest.

Improve the appearance of the admin panel, clarify the localization.

# RU
# Описание

**API-сервис для получения данных о первых 10 объявлениях по [ссылке](https://www.farpost.ru/vladivostok/service/construction/guard/+/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BD%D0%B0%D0%B1%D0%BB%D1%8E%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F/) с сервиса farpost.ru**

Проект разработан таким образом, чтобы его было легко расширять, тестровать и запускать в работу.

Выполнены все работы по предварительной настройке CI/CD.

Проект легко запустить локально с помощью docker-compose.

# Cтек
![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/-Django_REST_FRAMEWORK-black?style=for-the-badge&logo=Django)
![Scrapy](https://img.shields.io/badge/-Scrapy-black?style=for-the-badge&logo=Scrapy)
![Nginx](https://img.shields.io/badge/-Nginx-black?style=for-the-badge&logo=Nginx)
![Docker](https://img.shields.io/badge/-Docker-black?style=for-the-badge&logo=Docker)
![Swager](https://img.shields.io/badge/-Swager-black?style=for-the-badge&logo=Swager)
![GitHub](https://img.shields.io/badge/-GitHub_Actions-black?style=for-the-badge&logo=GitHub)


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

### Идеи по развитию

Добработать логику парсера, сейчас два запроса, можно объеденить в один скрипт для генерации JSON, также добавить логику для исключения дулбикатов объекта автора в БД при импорте фикстур.

Написать тесты, например, на Pytest.

Улучшить внешний вид админ панели, уточнить локализацию.

# Автор
## Александр Бучельников

[![Personal-Website](https://img.shields.io/badge/-Personal_website-black?style=for-the-badge&logo=)](https://buchelnikov.ddns.net/)

## Contact me

[![Telegram](https://img.shields.io/badge/-Telegram-black?style=for-the-badge&logo=Telegram)](https://t.me/aleksandr_buchelnikov)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black?style=for-the-badge&logo=LinkedIn)](https://www.linkedin.com/in/aleksandr-buchelnikov/)
[![E-mail](https://img.shields.io/badge/-E_mail-black?style=for-the-badge&logo=Gmail)](mailto:al.buchelnikov@gmail.com)