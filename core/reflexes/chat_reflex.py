from sockpuppet.reflex import Reflex
from sockpuppet.channel import Channel
from django.core.cache import cache
from django.utils import timezone


class ChatReflex(Reflex):
    def post(self, color, message, message_id):
        chats = cache.get("chats", [])
        chats.append({
            'message': message,
            'message_id': message_id,
            'created_at': timezone.now()
        })
        cache.set("chats", chats)
        channel = Channel("chat")
        channel.dispatch_event({
            'name': 'chats:added',
            'detail': {'messagre_id': message_id}
        })
        channel.broadcast()
