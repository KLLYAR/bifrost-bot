import threading
import discord
from group import Group
from broadcaster import Broadcaster
from message import Message as MS
from receiver import Receiver

from sender import *
import json
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

class CustomClient(discord.Client):
    
    def __init__(self, sender: ISender) -> None:
        super().__init__(intents=intents)
        self._sender = sender
        
    async def on_message(self, message):
    
        if message.author == self.user or message.author.bot:
            return

        await self._sender.send(json.dumps(MS(message).get_data()))
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_guild_channel_delete(self, channel):
        pass
    
class Custom2Client(discord.Client):
    
    def __init__(self) -> None:
        super().__init__(intents=intents)
        self.loop = asyncio.get_event_loop()
    
    def entrypoint(self, group):
    
        r = Receiver(Broadcaster(self, group))    
        self.loop.create_task(r.start())
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
       
        test_group = Group()
        test_group.add_channel(1043287494038392922)
        test_group.add_channel(1043238828019822733)
        test_group.add_channel(1043282193427992586)
        
        x = threading.Thread(target=self.entrypoint, args=(test_group,), daemon=True)
        x.start()