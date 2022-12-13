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
    
    @abstractmethod
    async def get_queue_name(self):
        pass

class Receiver(IReceiver):
    
    def __init__(self, queue_name: str, broadcaster: IBroadcaster):
        
        self._queue_name = queue_name        
        self._broadcaster = broadcaster
    
    def get_queue_name(self) -> str:
        return self._queue_name
    
    async def _callback(self, message: AbstractIncomingMessage) -> None:
        
        print(" [x] Message received!")
        
        await self._broadcaster.send(json.loads(message.body))
        
    async def start(self, queue_name):
    
        connection = await connect("amqp://guest:guest@localhost/")        
        
        async with connection:
            channel = await connection.channel()

            queue = await channel.declare_queue(self._queue_name)

            await queue.consume(self._callback, no_ack=True)

            print(" [*] Waiting for messages. To exit press CTRL+C")
            await asyncio.Future()