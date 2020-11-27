from sockpuppet.reflex import Reflex
import requests


class BookSearchReflex(Reflex):
    def perform(self, query=""):
        resp = requests.get('http://openlibrary.org/search.json', params={'q':query})
        resp.raise_for_status()
        self.books = resp.json().get("docs", [])
        self.count = len(self.books)

