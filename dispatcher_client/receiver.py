from abc import ABC, abstractmethod
import json

from broadcaster import IBroadcaster
import asyncio

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage


class IReceiver(ABC):

    @abstractmethod
    async def start(self):
        pass

class Receiver(IReceiver):
    
    def __init__(self, broadcaster: IBroadcaster):
        
        self._broadcaster = broadcaster
    
    async def _callback(self, message: AbstractIncomingMessage) -> None:
        
        print(" [x] Message received!")
        
        await self._broadcaster.send(json.loads(message.body))
        
    async def start(self):
    
        connection = await connect("amqp://guest:guest@localhost/")        
        
        async with connection:
            channel = await connection.channel()

            queue = await channel.declare_queue("hello")

            await queue.consume(self._callback, no_ack=True)

            print(" [*] Waiting for messages. To exit press CTRL+C")
            await asyncio.Future()