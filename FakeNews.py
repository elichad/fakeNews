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
import datetime
import json
from time import sleep
from secrets import *
import re
import soup
import predict
import filterEnglish

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

def getScore(url):
    return 0.9


N=3
SearchParameter='@fakenewsbotbrum'
print('Beginning For Loop')
results=tweepy.Cursor(api.search,q=SearchParameter).items()
tweets=[tweet for tweet in results]
print(len(tweets))
for tweet in tweepy.Cursor(api.search,q=SearchParameter).items():
    timeOfTweet=tweet._json['created_at']
    #print(tweet._json)
    dateTime=time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(timeOfTweet,'%a %b %d %H:%M:%S +0000 %Y'))
   
    #minuteOfTweet=dateTime.split(" ")[1].split(":")[1]
    #minuteOfTweet=int(minuteOfTweet)
    #minuteNow=datetime.datetime.now().minute
    #if minuteNow-minuteOfTweet>1:
    #    continue
    #hourOfTweet=dateTime.split(" ")[1].split(":")[0]
    #hourOfTweet=int(hourOfTweet)
    #hourNow=datetime.datetime.now().hour
    #if hourNow-hourOfTweet>1:
    #   continue
    
    sleep(1)
    tweet_txt=tweet._json['text']
    url_text = re.findall(r'href=[\'"]?([^\'" >]+)', tweet_txt) #From StackOverflow
    if url_text==[]:     
        try:
            url_text=tweet._json['entities']['urls'][0]['expanded_url']
        except:
            continue
        
    print ("hello there "+url_text)
    #url_text='http://www.bbc.co.uk/news/world-europe-42038801'
    if(url_text==[] or url_text==""): #just check again, why not
        continue
    Name=tweet._json['entities']['user_mentions'][0]['screen_name']
    
    Link= 'Link: ' +''
    text=soup.parse(url_text)[1]
    if text==-2:
        tweetText="@"+Name+" Sorry, I couldn't find an article in this page."
    elif text==-1:
        tweetText="@"+Name+" Sorry, I couldn't process that page."
    else:
        if filterEnglish.isEnglish(text):
            Score=predict.fakeNews(text)
            if(0.9<Score<=1.0):
                ScoreText='Extremely unreliable'
            elif(0.7<Score<=0.9):
                ScoreText='Very unreliable'
            elif(0.5<Score<=0.7):
                ScoreText='Somewhat unreliable.'
            elif(0.3<Score<=0.5):
                ScoreText='Somewhat reliable'
            elif(0.1<Score<=0.3):
                ScoreText='Very reliable'
            elif(0.0<Score<=0.1):
                ScoreText='Extremely reliable'
            tweetText="@" +Name+ " asked if "+url_text+ " is fake news: I think there's a " +str(round(Score*100)) +"% chance it's fake. "+ScoreText+"!"
        else:
            tweetText="@"+Name+" Sorry, it looks like this content isn't in English, so I can't analyse it."
    print(tweetText)
    #api.update_status(tweetText)
    
    #now retweet to get retweet count correct.
    #api.retweet(tweet['id'])
print('Finished For Loop')