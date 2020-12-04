from django.db import models


class CalendarEvent(models.Model):
    description = models.TextField()
    occurs_at = models.DateField()

    def __str__(self):
        return f"{self.occurs_at}"
