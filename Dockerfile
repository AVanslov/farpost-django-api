FROM python:3.9

WORKDIR /app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /app/scraper

RUN scrapy crawl farpost_author -O farpost_author.json
RUN scrapy crawl farpost -O farpost.json

WORKDIR /app/data

RUN python final_data_generator.py

WORKDIR /app/farpost

RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "farpost.wsgi"]