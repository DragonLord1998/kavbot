import requests


def dict(word):
    res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word)
    if res.status_code == 200:
        val = res.text
        return val
