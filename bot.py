import tweepy
import time

consumer_key= 't1eX5tAziIGuq5FYMTrHdFCHz'
consumer_secret= 'RI3XbBzn5VhGb8HwDhWVquWwPkbP8vio3pqhIieCmtLiZGLZ7C'
key= '1413201211545714690-EkQxCTxzF3zVvPAbeEWwxKcgHoBW0n'
secret= 'QbMnLarSBbXz9gdCk6983io1ffyK82YffepKafdjTZYXJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#random_tweets111' in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + "Thank you for testing my bot ", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
