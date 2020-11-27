from sockpuppet.reflex import Reflex
import requests


class BookSearchReflex(Reflex):
    def perfomance(self, query=""):
        
        resp = requests.get('http://openlibrary.org/search.json', params={'q':query})
        resp.raise_status()
        return resp.json().get("docs", [])

