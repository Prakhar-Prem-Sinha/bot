import tweepy
import time

consumer_key= 't1eX5tAziIGuq5FYMTrHdFCHz'
consumer_secret= 'RI3XbBzn5VhGb8HwDhWVquWwPkbP8vio3pqhIieCmtLiZGLZ7C'
key= '1413201211545714690-EkQxCTxzF3zVvPAbeEWwxKcgHoBW0n'
secret= 'QbMnLarSBbXz9gdCk6983io1ffyK82YffepKafdjTZYXJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "Java"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
