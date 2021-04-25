from sockpuppet.reflex import Reflex

from core.models import NewsletterSubscription


class SubscriptionReflex(Reflex):
    def add_person(self):
        o = NewsletterSubscription.objects.update_or_create(
            name=self.params['name'],
            email=self.params['email']
        )

    def remove_person(self):
        id = self.element.dataset['id']
        NewsletterSubscription.objects.filter(id=id).delete()
