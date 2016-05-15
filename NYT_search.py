import requests

NYT_key = "07cd2401d73889cfffb73cd6b5f83e49:8:75161073"

page = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json", params= ({
  'api-key': "07cd2401d73889cfffb73cd6b5f83e49:8:75161073",
  'q': "Apple"
}))


def Search(term):
    """ Will return a dictornary containing info from NYT data base based on relevent search term
        NOTE: this will pull the current days headlines 
    """
    page = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.json", params= ({
  'api-key': NYT_key,
  'q': term
}))
    return page.json()


def Search_Past(term, start, end):
    """ Will return a dictornary containing info from NYT data base based on relevent search term
        NOTE: will return all articles with the relivent search term bettwen the two dates
        give dates in YYYYMMDD format
    """
    page = requests.get("https://api.nytimes.com/svc/search/v2/articlesearch.sjon", params= ({
    'api-key': NYT_key,
    'q': term,
    'begin_date': start,
    'end_date': end
    }))
    return page.json()
