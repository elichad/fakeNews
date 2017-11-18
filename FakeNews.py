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
    #url_text = re.findall(r'href=[\'"]?([^\'" >]+)', tweet_txt) #From StackOverflow
    url_text='http://www.bbc.co.uk/news/world-europe-42038801'
    if(url_text==[]):
        break
    print(tweet._json['entities']['user_mentions'][0]['screen_name'])
    Name=tweet._json['entities']['user_mentions'][0]['screen_name']
    
    print(tweet_txt+ '\n')
    Link= 'Link: ' +''
    Score=0.9 #Placeholder value
    if(0<Score<=0.1):
        ScoreText='extremely unreliable.'
    elif(0.1<Score<=0.3):
        ScoreText='very unreliable.'
    elif(0.3<Score<=0.5):
        ScoreText='somewhat unreliable.'
    elif(0.5<Score<=0.7):
        ScoreText='somewhat reliable'
    elif(0.7<Score<=0.9):
        ScoreText='very reliable'
    elif(0.9<Score<=1.0):
        ScoreText='extremely reliable'
    api.update_status('@' +Name+ ' asked if '+url_text+ ' is fake news: Fake News Bot gives it a score of ' +str(Score) +', '+ScoreText+'!')
    
    #now retweet to get retweet count correct.
    #api.retweet(tweet['id'])
print('Finished For Loop \n')