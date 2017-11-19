#!/usr/bin/env python3

import pandas as pd
import scipy as sp
import time

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib

t0 = time.time()

articles = pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/fake_or_real_news.csv")
#articles = pd.read_csv("newData.csv")
train = articles

#train, test = train_test_split(articles, test_size=0.5)

labelTrain = train['label'].tolist()
#labelTest = test['label'].tolist()

count = CountVectorizer(stop_words='english', max_df=0.7)
 
countTrain = count.fit_transform(train['text'].tolist())
#countTest = count.transform(test['text'].tolist())

joblib.dump(count, 'features.pkl')
'''
tfidf = TfidfVectorizer(stop_words = 'english')

tfidfTrain = tfidf.fit_transform(test['text'].tolist())
tfidfTest = tfidf.transform(train['text'].tolist())
'''
#to re-add when count working

dfTrain = pd.DataFrame(countTrain.A, columns = count.get_feature_names())

trainFeatures = sp.column_stack((dfTrain[feature] for feature in count.get_feature_names()))

score = sp.array(labelTrain)

clf = MultinomialNB()

clf.fit(trainFeatures, labelTrain)

'''
dfTest = pd.DataFrame(countTrain.A, columns = count.get_feature_names())

testFeatures = sp.column_stack((dfTest[feature] for feature in count.get_feature_names()))
'''

joblib.dump(clf, 'fakeNews.pkl') 

clf2 = joblib.load('fakeNews.pkl')
'''
pred = clf2.predict()
predicted = clf2.predict_proba()

print pred
print predicted
'''
print()
print (time.time() - t0)
