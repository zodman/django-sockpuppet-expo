from django.views.generic.base import TemplateView
from .mixins import MixinBase


class BookSearch(MixinBase, TemplateView):
    template_name="book_search.html"
    files = (
        ('core/reflexes/book_search_reflex.py', 'python3'),
        ('core/views/book_search.py', 'python3'),
        ('core/javascript/controllers/book_search_controller.js', 'typescript'),
        ('core/templates/book_search.html', 'htmldjango'),
    )

book_search = BookSearch.as_view()
