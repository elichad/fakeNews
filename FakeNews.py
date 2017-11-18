#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:09:34 2017

Author: Julian Hewitt

This is where the code for the Fake News bot goes, probably. Made during BrumHack 7.0 .
Based on example code by Molly White, thanks Molly!
"""
import tweepy
from secrets.py import *

auth=tweepy.OAuthHandler(C_KEY,C_SECRET)
auth.set_access_token(A_TOKEN,A_TOKEN_SECRET)
api=tweepy.API(auth)