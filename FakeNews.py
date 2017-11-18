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
#N=1000
#for tweet in Tweepy.Cursor(api.search,q='@fakenewsbotbrum').items(N):
 #   tweet=str(tweet)
  #  raise Exception('exit')
   # Link= 'Link: ' +''
   # api.update_status(tweet)
    
    #now retweet to get retweet count correct.
    #api.retweet(tweet['id'])