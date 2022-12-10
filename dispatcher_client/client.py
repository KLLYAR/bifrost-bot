import threading
import discord
from group import Group
from broadcaster import Broadcaster
from receiver import Receiver
import asyncio

class DispatcherClient(discord.Client):
    
    def __init__(self) -> None:
        
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.guilds = True
        
        super().__init__(intents=intents)
        self.loop = asyncio.get_event_loop()
    
    def entrypoint(self, group):
    
        r = Receiver(Broadcaster(self, group))    
        self.loop.create_task(r.start())
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
       
        test_group = Group()
        
        
        
        x = threading.Thread(target=self.entrypoint, args=(test_group,), daemon=True)
        x.start()