from sockpuppet.reflex import Reflex
import datetime
from core.models.event import CalendarEvent


class CalendarReflex(Reflex):
    def new_calendar_event(self):
        date_element = self.element.dataset["date"]
        occurs_at = datetime.date.fromisoformat(date_element)
        self.calendar_event = CalendarEvent(occurs_at=occurs_at, description='lorem').save()

