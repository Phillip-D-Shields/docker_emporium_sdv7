# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@email.com 
ENV DJANGO_SUPERUSER_PASSWORD=P@ssw0rd1 
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
COPY . /code/

