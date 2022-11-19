from abc import ABC, abstractmethod

from aio_pika import Message, connect

class ISender(ABC):
    
    @abstractmethod
    async def send(self, data):
        pass

class Sender(ISender):

    async def send(self, data):
        
        connection = await connect("amqp://guest:guest@localhost/")

        async with connection:
            
            channel = await connection.channel()

            queue = await channel.declare_queue("hello")

            await channel.default_exchange.publish(
                message=Message(data.encode('utf-8')),
                routing_key=queue.name,
            )

            print(" [x] Message sent!")
        
        await connection.close()