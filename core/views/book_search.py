from django.views.generic.base import TemplateView
from django.conf import settings
import os

BASE_PATH = settings.BASE_DIR

class BookSearch(TemplateView):
    template_name="book_search.html"
    files = (
        ('core/reflexes/book_search_reflex.py', 'python3'),
        ('core/views/book_search.py', 'python3'),
        ('core/javascript/controllers/book_search_controller.js', 'typescript'),
    )

    def get_files(self):
        path_ = lambda x: open(os.path.join(BASE_PATH, x)).read()
        return [dict(src=path_(i[0]), type=i[1], name=i[0]) for i in self.files]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = self.get_files()
        return context

book_search = BookSearch.as_view()
