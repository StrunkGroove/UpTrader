FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r requirements.txt