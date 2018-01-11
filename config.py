import os
import kombu.transport
# Twitter
twitter_consumer_key = os.environ['TWITTER_CONSUMER_KEY']
twitter_consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
twitter_access_token_secret = os.environ['TWITTER_TOKEN_SECRET']

tweets_per_session = 10

# Celery
celery_broker = os.environ.get('CELERY_BROKER', 'redis://localhost')

# Bot specific
sentences_file = os.environ.get('SENTENCES_FILE', 'sentences.txt')
