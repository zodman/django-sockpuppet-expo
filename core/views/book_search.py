from django.views.generic.base import TemplateView
from .mixins import MixinBase


class BookSearch(MixinBase, TemplateView):
    demo_template = "_book_search_demo.html"
    subtitle = 'Search Book'
    files = (
        ('core/reflexes/book_search_reflex.py', 'python', 'python3'),
        ('core/views/book_search.py', 'python', 'python3'),
        ('core/javascript/controllers/book_search_controller.js', 'javascript', 'javascript'),
        ('core/templates/_book_search_demo.html', 'html', 'htmldjango'),
    )

book_search = BookSearch.as_view()
