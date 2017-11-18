from newspaper import Article
import pandas as pd

def parse(pageURL):
    article=Article(pageURL,language='en')
    article.download()
    article.parse()
    source=pageURL.split('/')[2]
    
    pars=article.text.split("\n")
    
    i=0
    firstPar=pars[i]
    while firstPar.lower().find("image")!=-1 or firstPar=='':
        i+=1
        firstPar=pars[i]
    #save output
    #order: source site, title, first paragraph
    return [article.title,article.text]

pageURL='http://www.bbc.co.uk/news/uk-england-nottinghamshire-42037305'
content=parse(pageURL)
"""
for i in range(len(urls)):
    url=urls[i]
    print(url)
    src,title,par=parsePage(url)
    dfout.loc[len(df)]=[title,par,fakenesses[i]]
    
print(dfout)
dfout.to_csv('testData.csv')
"""