import requests
from bs4 import BeautifulSoup

def quotes():
    res = requests.get("https://zenquotes.io/api/quotes/")
    if res.status_code == 200:
        val= res.json()
        quote = (val[0]['q'])
    return quote