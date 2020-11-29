from django.views.generic.base import TemplateView
from .mixins import MixinBase

class ChatView(MixinBase, TemplateView):
    demo_template = '_chat_demo.html'
    subtitle = 'Chat'
    files = (
        ('core/views/chat.py', 'python', 'python3'),
        ('core/reflexes/chat_reflex.py', 'python', 'python3'),
        ('core/javascript/controllers/chat_controller.js', 'javascript', 'javascript'),
        ('core/templates/_chat_demo.html', 'html', 'htmldjango'),
    )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['chats'] = [dict(message='message1')]
        return context

chat = ChatView.as_view()


