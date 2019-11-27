FROM python:3.7.5-stretch

RUN apt-get update

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app
