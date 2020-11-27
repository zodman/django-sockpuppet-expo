from django.views.generic.base import TemplateView


class BookSearch(TemplateView):
    template_name="book_search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_count"] = 0
        return context

book_search = BookSearch.as_view()
