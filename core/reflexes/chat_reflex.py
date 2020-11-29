from sockpuppet.reflex import Reflex
from sockpuppet.channel import Channel
from django.core.cache import cache
from django.utils import timezone


class ChatReflex(Reflex):
    def post(self, color, message, message_id):
        chats = cache.get("chats", [])
        self.total = 100
        if len(chats) > self.total:
            chats = []
        if message:
            chats.append({
                'message': message,
                'messageId': message_id,
                'created_at': timezone.now()
            })
            cache.set("chats", chats)
            channel = Channel("ChatChannel")
            channel.dispatch_event({
                'name': 'chats:added',
                'detail': {'messageId': message_id}
            })
            channel.broadcast()
