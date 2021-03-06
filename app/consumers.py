from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

import asyncio
import json
import time
from datetime import datetime
import pytz

class clock(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.start_periodic_task()

    async def start_periodic_task(self):
        while True:
            bucharest = pytz.timezone('Europe/Bucharest')
            now_local = datetime.now(tz=bucharest)
            current_time = now_local.strftime("%H:%M:%S - %d/%m/%Y -") + " Europe/Bucharest"
            #now = datetime.now()
            #current_time = now.strftime("%H:%M:%S")
            await self.send(text_data=json.dumps({
               'message': current_time
            }))
            await asyncio.sleep(1)


#syncron
class EchoConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send(text_data='connected')

    def receive(self, *, text_data):
        print(text_data)
        self.send(text_data="echo: "+text_data)

    def disconnect(self, message):
        print('disconnect')

class AsyncEchoConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.n  = 0

        self.group_name = "mygroup"

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )        

        await self.accept()
        await self.send(text_data='connected')

    async def receive(self, *, text_data):
        self.n += 1
        print(text_data)

        #this below will send message only to the sender socket not to group
        #await self.send(text_data="echo: "+ str(self.n) + " " + text_data)

        # Send message to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'group_message',  #this is sending pocedure name
                'message': text_data,
                'n': self.n
            }
        )
  
    # Sending message to group
    async def group_message(self, event):
        message = event['message']
        n = event['n']

        await self.send(text_data="echo: "+ str(n) + " " + message)


    async def disconnect(self, message):

        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        print('disconnect')





