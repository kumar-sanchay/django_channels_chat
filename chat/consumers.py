import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class Consumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_name)
        print(self.user)
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data['user'])
        print(data['message'])
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': data['user'],
                'message': data['message'],
            }
        )

    def chat_message(self, event):
        message = event['message']
        user = event['user']
        self.send(text_data=json.dumps({
            'message': message,
            'user': user,
        }))