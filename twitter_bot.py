import tweepy
import time
import os
from os import environ


consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

#print(user)

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name, file=open("output.txt", "a", encoding='utf-8'))
    
