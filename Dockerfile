FROM python:3.6-slim

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt && chown -R daemon /usr/src/app

USER daemon

CMD [ "celery", "-A", "publisher", "worker", "--loglevel=info", "--beat"]
