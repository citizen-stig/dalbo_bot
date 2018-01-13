import random
from celery import Celery
from celery.schedules import crontab
import markovify
import tweepy

import config

app = Celery(
    'dalbo_bot',
    broker=config.celery_broker,
    task_serializer='json',
)
app.conf.beat_schedule = {
    'generate-tweets': {
        'task': 'publisher.generate_tweets',
        'schedule': crontab(hour=7,
                            minute=30,
                            day_of_week='mon,wed,thu,fri'),
    },
}
app.conf.timezone = 'UTC'


@app.task
def post_to_twitter(message):
    auth = tweepy.OAuthHandler(
        config.twitter_consumer_key,
        config.twitter_consumer_secret)
    auth.set_access_token(
        config.twitter_access_token,
        config.twitter_access_token_secret)
    api = tweepy.API(auth)
    result = api.update_status(message)
    return result


def get_random_delay():
    return random.randint(300, 3600)


@app.task
def generate_tweets():
    sentences = open(config.sentences_file).read()
    # Build the model.
    text_model = markovify.Text(sentences)
    base_delay = random.randint(100, 200)
    for _ in range(config.tweets_per_session):
        delay = base_delay + get_random_delay()
        base_delay += delay
        sentence = text_model.make_sentence()
        post_to_twitter.apply_async(
            (sentence,),
            countdown=delay)
