#!/home/mm/anaconda3/envs/automate/bin/python
import configparser
import random
import datetime
import time

from twython import Twython
import markovify


config = configparser.ConfigParser()
# Make sure to point config.read to the file
config.read('twitter1.ini')

consumer_key = config.get('twitter', 'CONSUMER_KEY')
consumer_secret = config.get('twitter', 'CONSUMER_SECRET')
oauth_access_token = config.get('twitter', 'oauth_token')
oauth_access_secret = config.get('twitter', 'oauth_secret')

twitter = Twython(consumer_key, consumer_secret,
                  oauth_access_token, oauth_access_secret)

# Get raw text as string.
with open("trump_corpus.txt") as f:
    text = f.read()

# Seed Random with date
random.seed(datetime.datetime.now())

# Build the model
text_model = markovify.Text(text, state_size=2)

# find random thing to tweet
def random_gen():
    list_poss_tweets = []
    for i in range(0, 100):
        new_sentence = text_model.make_short_sentence(140)
        list_poss_tweets.append(new_sentence)
    return list_poss_tweets


while True:

    # Handle exceptions:
    # twython.exceptions.TwythonError: Twitter API returned a 403 (Forbidden), Status is a duplicate.
    try:
        # Make time to sleep vary to make it look sort of real
        time_to_sleep = random.randint(1684, 3609)
        # Get the list of Possible Tweets
        possible_tweets = random_gen()
        # Generate a random number to grab a possible tweet and send off...
        new_status_num = random.randint(0, 99)
        twitter.update_status(status=possible_tweets[new_status_num])
        time.sleep(time_to_sleep)
    except Exception as exp:
        # Not really handling anything... just keep running until you find one that is not a dup
        print('Handling run-time exception:', exp)
    finally:
        print('and Finally, Good night sweet Prince!')