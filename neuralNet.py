#!/usr/bin/env python3

import pandas as pd
import scipy as sp
import time

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


t0 = time.time()



df = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/fake_or_real_news.csv")

train, test = train_test_split(df, test_size=0.2)

score = train['score'].tolist()

count = CountVectorizer(stop_words='english')

coutTrain = count.fit_transform(test['text'].tolist())
coutTest = count.transform(train['text'].tolist())

tfidf = TfidfVectorizer(stop_words = 'english')

tfidfTrain = tfidf.fit_transform(test['text'].tolist())
tfidfTest = tfidf.transform(train['text'].tolist())


clf = MultinomialNB()

clf.fit(coutTrain, score)



print time.time() - t0

'''
import time

def getFeatures(df):
    source = sp.array(df['source'].tolist())
    title = sp.array(df['title'].tolist())
    #return sp.column_stack(([0,0,0],[0,0,0]))
    return sp.column_stack((source, title))

articles = pd.read_csv('testdata.csv', sep = ',')

features = getFeatures(articles)

fakeness = sp.array(articles['fakeness'].tolist())


clf = MLPRegressor()

t0 = time.time()

clf.fit(features, fakeness)

print time.time() - t0

'''