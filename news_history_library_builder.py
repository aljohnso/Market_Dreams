import newspaper
import datetime

URL = 'http://www.reuters.com/news/archive/worldNews?date='

def getPaper(date):
    URL = 'http://www.reuters.com/news/archive/worldNews?date='
    URL = URL + str(date)
    print(URL)
    paper = newspaper.build(URL)
    print(paper)
    articles_ = paper.articles
    print(articles_)
    i=0
    acticles_[i].download()
    articles_[i].parse()
    articles_   [i].nlp()
    print(articles[i].keywords)