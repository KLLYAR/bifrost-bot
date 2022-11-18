import discord
from group import Group
from broadcaster import Broadcaster
from message import Message

intents = discord.Intents.default()
intents.message_content = True

class CustomClient(discord.Client):
    
    def __init__(self) -> None:
        super().__init__(intents=intents)
        self._setup()
        
    def _setup(self):
        ads_group = Group()
        ads_group.add_channel(1043063977070047272)
        ads_group.add_channel(1042960076304031876)

        self.ads_broadcaster = Broadcaster(self, ads_group)
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        
    async def on_message(self, message):
    
        if message.author == self.user or message.author.bot:
            return

        if(await self.ads_broadcaster.send(Message(message))): 
            await message.delete() # Slow