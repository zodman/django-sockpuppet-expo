from django.views.generic.base import TemplateView
from .mixins import ExampleMixin

class ExampleView(ExampleMixin, TemplateView):
    demo_template = '_example_demo.html'
    subtitle = 'Increment'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.request.session.get("count", 0)
        return context

example = ExampleView.as_view()


