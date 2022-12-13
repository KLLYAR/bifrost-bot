from nextcord import Interaction, Embed
from nextcord.ext import commands
import nextcord
import json
from message_formatter import MessageFormatter as MS
from channel_group_manager import *
from sender import * 

from nextcord import Message

class MessageCog(commands.Cog):
    def __init__(self, client, sender: ISender):
        self.client = client
        self._sender = sender
        
    @commands.Cog.listener()
    async def on_message(self, message: Message):
        
        if message.author == self.client or message.author.bot:
            return
        
        has_channel, token = self.client.get_channel_group_manager().has_channel(message.channel.id)
        if has_channel:
            await self._sender.send(token, json.dumps(MS(message).get_data()))
        
        
        # await message.add_reaction(emoji=824906654385963018)
def setup(client):
    client.add_cog(MessageCog(client, Sender()))