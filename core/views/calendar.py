from django.views.generic.base import TemplateView
from django.template.loader import render_to_string
from django import forms
import calendar as calendarmod
from datetime import date
import datetime
from .mixins import CalendarMixin
from core.models.event import CalendarEvent

class CustomCalendar(calendarmod.HTMLCalendar):
    def formatmonth(self, year, month, withyear=True, events=[]):
        self.year = year
        self.month = month
        self.events = events
        return super().formatmonth(year, month, withyear)

    def formatday(self, day, weekday):
        context = {
            "day": day,
            "date": date(self.year, self.month, day) if day > 0 else None,
            "css_class": self.cssclass_noday if day == 0 else self.cssclasses[weekday],
            "calendar_events": self.events,
            "now": date.today(),
        }
        return render_to_string("_td_calendar.html", context)


attrs = {
    'data-target':'calendar.input',
}

class FormEvent(forms.Form):
    event_hour = forms.CharField(widget=forms.HiddenInput(attrs=attrs))
    event_meridian = forms.CharField(widget=forms.HiddenInput(attrs=attrs))
    description = forms.CharField(widget=forms.Textarea())


class CalendarView(CalendarMixin, TemplateView):
    demo_template = "_calendar.html"
    subtitle = "Calendar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_str = self.request.GET.get("date", "")
        if date_str:
            today = datetime.datetime.fromisoformat(date_str).date()
        else:
            today = date.today()
        events = [
            # {"date": today, "description": "lorem ipsum"},
            # {"date": date(2020, 12, 9), "description": "lorem ipsum"},
            # {"date": date(2020, 12, 9), "description": "lorem ipsum"},
            # {"date": date(2020, 12, 13), "description": "lorem ipsum"},
            # {"date": date(2020, 12, 15), "description": "lorem ipsum"},
            # {"date": date(2020, 12, 15), "description": "lorem ipsum"},
            # {"date": date(2020, 12, 15), "description": "lorem ipsum"},
        ]
        context["calendar"] = CustomCalendar().formatmonth(
            today.year, today.month, events=events
        )
        context['calendar_event'] = CalendarEvent()
        context["next_month_date"] = today + datetime.timedelta(days=30)
        context["prev_month_date"] = today + datetime.timedelta(days=-30)
        context["hours"] = [str(i) for i in range(1, 13)]
        context["form"] = FormEvent()
        return context


calendar = CalendarView.as_view()
