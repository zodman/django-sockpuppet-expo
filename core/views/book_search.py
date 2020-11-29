from django.views.generic.base import TemplateView
from .mixins import BookSearchMixin


class BookSearch(BookSearchMixin, TemplateView):
    demo_template = "_book_search_demo.html"
    subtitle = 'Search Book'

book_search = BookSearch.as_view()
