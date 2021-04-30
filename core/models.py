from django.db import models


class NewsletterSubscription(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)
