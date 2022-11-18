import discord
from group import Group
from broadcaster import Broadcaster
from message import Message

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

class CustomClient(discord.Client):
    
    def __init__(self) -> None:
        super().__init__(intents=intents)
        self._setup()
        
    def _setup(self):
        self._dark_cafe = Group()
        self.ads_broadcaster = Broadcaster(self, self._dark_cafe)
        
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        
    async def on_message(self, message):
    
        if message.author == self.user or message.author.bot:
            return

        if(await self.ads_broadcaster.send(Message(message))): 
            await message.delete() # Slow
            
    async def on_guild_channel_delete(self, channel):
        if channel.id in self._ads_group:
            self._ads_group.remove_channel(channel.id)