import requests


def dict(word):
    res = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word)
    if res.status_code == 200:
        val= res.json()
        valdict ={
            'meaning': (val[0]['meanings'][0]['definitions'][0]['definition']),
            'example':  (val[0]['meanings'][0]['definitions'][0]['example'])
        }
        return(valdict)

