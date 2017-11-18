#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:09:34 2017

Author: Julian Hewitt

This is where the code for the Fake News bot goes, probably. Made during BrumHack 7.0 .
Based on example code by Molly White, and Lisa Tagliaferri.
"""
import tweepy
import time
import json
from time import sleep
from secrets import *
import re
auth=tweepy.OAuthHandler(C_KEY,C_SECRET)
auth.set_access_token(A_TOKEN,A_TOKEN_SECRET)
api=tweepy.API(auth)


ID=api.me()._json['id']
print(ID)
#api.update_status('TEST')
#sleep(100000)

#periodically look for all mentions of myself, anticipate less than N mentions
#need to make new tweet with text of old tweet inside it, then do a blank retweet.
#retweeting with own additions doesn't work within Twitter API for some reason.

#####Tweet Every Line of the Bee Movie
#BeeMovie=open('BeeMovie.txt','r')
#Lines=BeeMovie.readlines()
#for x in Lines:
#    if x.rstrip():
        # api.update_status(x)
#        print(x)
#####Tweet Every Line of the Bee Movie



N=1
SearchParameter='@fakenewsbotbrum'
print('Beginning For Loop \n')
for tweet in tweepy.Cursor(api.search,q=SearchParameter).items(N):
    sleep(1)
    tweet_txt=tweet._json['text']
    url_text= re.search("(?P<url>https?://[^\s]+)", myString).group("url") #From StackOverflow
    Name=tweet._json['screen_name']
    
    print(tweet_txt+ '\n')
    Link= 'Link: ' +''
    api.update_status('@' +Name+ 'asked if'+url_txt+ ' is fake news: Fake News Bot gives it a score of' )
    
    #now retweet to get retweet count correct.
    #api.retweet(tweet['id'])
print('Finished For Loop \n')