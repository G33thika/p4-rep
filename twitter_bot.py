import tweepy
import time
import os
from os import environ
import mysql.connector 



consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

db = environ['db']
user = environ['username']
dbpass = environ['dbpass']
host = environ['host']


mydb = mysql.connector.connect(host = host, user = user, password = dbpass, database= db)

mycursor = mydb.cursor()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


for follower in tweepy.Cursor(api.followers).items():
    # print(follower.name, file=open("ou.txt", "a", encoding='utf-8'))
    query = "INSERT INTO followers (id, name) VALUES (%s, %s);"
    data = (follower.id , follower.name)

    try:
        mycursor.execute(query, data)
        mydb.commit()
    except Exception as error:
        pass