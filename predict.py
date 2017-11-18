#!/usr/bin/env python3

import pandas as pd
import scipy as sp
import time

#from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

def fakeNews(data):
    t0 = time.time() 
        
    count = joblib.load('features.pkl')
    clf = joblib.load('fakeNews.pkl')
    
    test = articles.loc[0]
    
    feature = count.transform([test['text'],test['text']])
    
    dfTest = pd.DataFrame(feature.A, columns = count.get_feature_names())
    
    trainFeatures = sp.column_stack((dfTest[feature] for feature in count.get_feature_names()))
    
    predicted = clf.predict_proba(trainFeatures)
        
    print time.time() - t0

    return predicted[0][1]

articles = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/fake_or_real_news.csv")

data = articles.loc[1]

print fakeNews(data)