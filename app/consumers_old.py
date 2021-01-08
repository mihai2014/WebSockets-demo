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
        await self.accept()
        await self.send(text_data='connected')

    async def receive(self, *, text_data):
        self.n += 1
        print(text_data)
        await self.send(text_data="echo: "+ str(self.n) + " " + text_data)

    async def disconnect(self, message):
        print('diconnect')

