from django.forms import ModelForm
from django.views.generic.edit import FormView

from core.models import NewsletterSubscription
from core.views.mixins import NewsletterSignupMixin


class NewsletterSubscriptionForm(ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name', 'email']


class NewsletterSignupView(NewsletterSignupMixin, FormView):
    demo_template = '_newsletter_signup.html'
    form_class = NewsletterSubscriptionForm
    subtitle = 'Newsletter Signup'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['people'] = NewsletterSubscription.objects.all()
        return context


view = NewsletterSignupView.as_view()
