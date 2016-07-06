#!/usr/bin/python
# -*- coding: utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import cloudant_uploader

# Twitter Keys
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

class StdOutListener(StreamListener):

    def on_data(self, data):
        cloudant_uploader.insertTweet(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['saraiva.com.br', 'www.saraiva.com.br', 'www.livrariasaraiva.com.br', 'saraiva'])