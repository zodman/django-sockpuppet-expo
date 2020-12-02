from django.views.generic.base import TemplateView
from .mixins import ExampleMixin

class CalendarView(ExampleMixin, TemplateView):
    demo_template = '_calendar.html'
    subtitle = 'Calendar'

calendar = CalendarView.as_view()


    
