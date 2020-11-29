from sockpuppet.reflex import Reflex
import requests


class BookSearchReflex(Reflex):
    def perform(self, query=""):
        resp = requests.get("http://openlibrary.org/search.json", params={"q": query})
        resp.raise_for_status()
        books = resp.json()
        self.books = books.get("docs", [])
        self.count = books["num_found"]
