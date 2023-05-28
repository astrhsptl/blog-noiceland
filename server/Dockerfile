FROM python:3.10-alpine as builder
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache python3 postgresql-libs libxml2-dev libxslt-dev 
RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

COPY ./ .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

FROM python:3.10-alpine

WORKDIR /app

RUN apk add libpq

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache /wheels/*

COPY ./ .