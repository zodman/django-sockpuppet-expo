from django.forms import ModelForm
from django.views.generic.edit import FormView

from core.models import NewsletterSubscription


class NewsletterSubscriptionForm(ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name', 'email']


class YourReflexNameView(FormView):
    template_name = '_newsletter_signup.html'
    form_class = NewsletterSubscriptionForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['people'] = NewsletterSubscription.objects.all()
        return context


view = YourReflexNameView.as_view()
