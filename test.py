from bs4 import BeautifulSoup
import urllib.request as urllib2
import praw
def findInfoYahoo(stockname):
    """ Will find the headlines from yahoo finance for a given stockname
    """
    url = 'http://in.finance.yahoo.com/q?s=' + stockname
    data = urllib2.urlopen(url)
    soup = BeautifulSoup(data)

    divs = soup.find('div',attrs={'id':'yfi_headlines'})
    div = divs.find('div',attrs={'class':'bd'})
    ul = div.find('ul')
    lis = ul.findAll('li')
    hls = []

    for li in lis:
        headlines = li.find('a').contents[0]
        print( str(headlines))



def getTopReddit(companyName):
  """ Will get the top 10 comments from reddits API
  """
  r = praw.Reddit(user_agent='my_cool_application')
  submissions = r.get_subreddit(companyName).get_hot(limit=10)
  a = [str(x) for x in submissions]
  print(a)


