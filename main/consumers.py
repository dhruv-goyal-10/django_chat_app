import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from .serializers import MessageSerializer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        group_name = self.room_name
        author = text_data_json["author"]
        content = text_data_json["content"]
        serializer = MessageSerializer(
            data={"group_name": group_name, "author": author, "content": content}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        data.update({"type": "chat.message"})

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, data)

    # Receive message from room group
    def chat_message(self, event):
        print(123, event)
        print(type(event))
        print(json.dumps(event))
        self.send(text_data=json.dumps(event))
