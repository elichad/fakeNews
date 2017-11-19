#!/usr/bin/env python3

import pandas as pd
import scipy as sp
import time

#from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

def fakeNews(text):
    t0 = time.time() 
        
    count = joblib.load('features.pkl')
    clf = joblib.load('fakeNews.pkl')
    
    feature = count.transform([text,text])
 
    dfTest = pd.DataFrame(feature.A, columns = count.get_feature_names())

    trainFeatures = sp.column_stack((dfTest[feature] for feature in count.get_feature_names()))

    predicted = clf.predict_proba(trainFeatures)
        
    print(time.time() - t0)

    return predicted[0][0]

