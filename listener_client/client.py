import discord
from message import Message as MS
from sender import *
import json

class CustomClient(discord.Client):
    
    def __init__(self, sender: ISender) -> None:
        
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.guilds = True
        
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