from newspaper import Article
import pandas as pd
import sys

def parse(pageURL):
    try:
        article=Article(pageURL,language='en')
        article.download()
        article.parse()
        if article.text=='':
            print ("No article found")
            return -2
        return [article.title,article.text]
    except:
        print("Unexpected error: ",sys.exc_info()[0])
        return -1
    """
    source=pageURL.split('/')[2]
    
    pars=article.text.split("\n")
    
    i=0
    firstPar=pars[i]
    while firstPar.lower().find("image")!=-1 or firstPar=='':
        i+=1
        firstPar=pars[i]
        """
    #save output
    #order: source site, title, first paragraph
   

pageURL='http://www.bbc.co.uk/news/uk-england-nottinghamshire-42037305'
#pageURL='http://www.youtube.com'
content=parse(pageURL)
print(content)
if content==-1:
    print("no")
    #Sorry, there was an error trying to read that link.
elif content==-2:
    print("hell no")
    #Sorry, I couldn't find any article content.
else: #success????
    print("hi there friend, here's ur results")
    #do fake news function
    
"""
for i in range(len(urls)):
    url=urls[i]
    print(url)
    src,title,par=parsePage(url)
    dfout.loc[len(df)]=[title,par,fakenesses[i]]
    
print(dfout)
dfout.to_csv('testData.csv')
"""