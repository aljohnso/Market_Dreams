from bs4 import BeautifulSoup
import urllib.request as urllib2
import praw
def findInfoYahoo(stockname):
#http://stackoverflow.com/questions/22330467/scraping-headlines-from-yahoo-finance-using-python
    """ Will find the headlines from yahoo finance for a given stockname
    """
    url = 'http://in.finance.yahoo.com/q?s=' + stockname
    data = urllib2.urlopen(url)
    soup = BeautifulSoup(data, lxml)

    divs = soup.find('div',attrs={'id':'yfi_headlines'})
    div = divs.find('div',attrs={'class':'bd'})
    ul = div.find('ul')
    lis = ul.findAll('li')
    hls = []

    for li in lis:
        headlines = li.find('a').contents[0]
        print( str(headlines))



def getTopReddit(companyName, numcomments = 10):
  """ Will get the top 10 comments from reddits API
  """
  r = praw.Reddit(user_agent='my_cool_application')
  submissions = r.get_subreddit(companyName).get_hot(limit=numcomments)
  a = [str(x) for x in submissions]
  print(a)

def CNN():
#http://stackoverflow.com/questions/22330467/scraping-headlines-from-yahoo-finance-using-python
    """ Will scrape the headlines off cnn.com
    """
    url = 'http://www.cnn.com'
    data = urllib2.urlopen(url)
    soup = BeautifulSoup(data, 'lxml')

    headlines = soup.find_all(attrs={"class": "cd__headline-text"})
    # print (headlines)
    for node in headlines:
      print(node.text)


def NY_times():
    """ Will scrape the headlines off cnn.com
    """
    url = 'http://www.cnn.com'
    data = urllib2.urlopen(url)
    soup = BeautifulSoup(data, 'lxml')

    headlines = soup.find_all(attrs={"class": "cd__headline-text"})
    # print (headlines)
    for node in headlines:
      print(node.text)
