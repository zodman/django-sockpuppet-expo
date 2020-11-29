from django.views.generic.base import TemplateView
from django.core.cache import cache
from .mixins import ChatMixin

class ChatView(ChatMixin, TemplateView):
    demo_template = '_chat_demo.html'
    subtitle = 'Chat'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['chats'] = cache.get("chats", [])
        return context

chat = ChatView.as_view()


