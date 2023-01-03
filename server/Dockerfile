FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg
RUN apk add postgresql-dev

RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "/app/entrypoint.sh" ]