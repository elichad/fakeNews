import urllib
from newspaper import Article
from bs4 import BeautifulSoup
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
    return [source,article.title,firstPar]


http=urllib3.PoolManager()
#pageURL='http://www.bbc.co.uk/news/42032629'
#pageURL='http://www.foxnews.com/us/2017/11/18/police-officer-slain-near-pittsburgh-gunman-still-at-large.html'
#pageURL='http://www.theguardian.com/society/2017/nov/18/lords-push-for-children-to-be-protected-against-tech-giants-by-law'
response=http.request('GET',pageURL)

data=[['http://www.bbc.co.uk/news/42032629',0],['http://www.foxnews.com/us/2017/11/18/police-officer-slain-near-pittsburgh-gunman-still-at-large.html',0.5],['http://www.theguardian.com/society/2017/nov/18/lords-push-for-children-to-be-protected-against-tech-giants-by-law',0]]

df=pd.DataFrame(columns=['source','title','firstPar','fakeness'])
for i in range(len(data)):
    src,title,par=parse(data[i][0])
    df.loc[len(df)]=[src,title,par,data[i][1]]

df.to_csv('testdata.csv')