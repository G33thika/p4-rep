import tweepy
import time
import os
from os import environ
import psycopg2



consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

db = environ['db']
user = environ['username']
dbpass = environ['dbpass']
host = environ['host']
port = environ['port']

conn = psycopg2.connect(
    database=db, user=user, password=dbpass, host=host, port=port
)


conn.autocommit = True

cursor = conn.cursor()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


for follower in tweepy.Cursor(api.followers).items():
    # print(follower.name, file=open("ou.txt", "a", encoding='utf-8'))
    query = "INSERT INTO followers (id, name) VALUES (%s, %s);"
    data = (follower.id , follower.name)

    try:
        cursor.execute(query, data)
        conn.commit()
    except Exception as error:
        pass

conn.close()