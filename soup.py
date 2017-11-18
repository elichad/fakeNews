import urllib
from newspaper import Article
from bs4 import BeautifulSoup

http=urllib3.PoolManager()
pageURL='http://www.bbc.co.uk/news/42032629'
#pageURL='http://www.foxnews.com/us/2017/11/18/police-officer-slain-near-pittsburgh-gunman-still-at-large.html'
response=http.request('GET',pageURL)
soup = BeautifulSoup(response.data, 'html.parser')

article=Article(pageURL,language='en')
article.download()
article.parse()

print(article.title)

#print(soup.prettify())

