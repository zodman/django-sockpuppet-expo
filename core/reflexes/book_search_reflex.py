from sockpuppet.reflex import Reflex
import requests


class BookSearchReflex(Reflex):
    def perform(self, query=""):
        resp = requests.get('http://openlibrary.org/search.json', params={'q':query})
        resp.raise_for_status()
        return resp.json().get("docs", [])

