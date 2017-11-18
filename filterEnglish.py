# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:33:59 2017

@author: elich
"""
import nltk
import pandas as pd

englishVocab=set(w.lower() for w in nltk.corpus.words.words())

def filterWords(text):
    textWords=nltk.wordpunct_tokenize(text)
    filteredWords=[]
    for word in textWords:
        if word.lower() in englishVocab:
            filteredWords.append(word)
    filteredText=" ".join(filteredWords)
    return filteredText

text="Return a dictionary of languages and their likelihood of being the natural language of the input text"
#text="El aeropuerto se considera como un aeródromo para el tráfico regular de aviones."

dfin=pd.read_csv("https://s3.amazonaws.com/assets.datacamp.com/blog_assets/fake_or_real_news.csv")

titles=dfin['title'].tolist()
texts=dfin['text'].tolist()
scores=dfin['label'].tolist()

dfout=pd.DataFrame(columns=["title","text","label"])

for i in range(len(titles)):
    dfout.loc[len(dfout)]=[filterWords(titles[i]),filterWords(texts[i]),scores[i]]

dfout.to_csv("filteredData.csv")

print("Complete")