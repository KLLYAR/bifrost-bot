import nextcord
from message_formatter import MessageFormatter as MS
from sender import *
from channel_group_manager import *
import json
from nextcord.ext import commands
from receiver import *
from async_task_manager import *

class BotClient(commands.Bot):
    
    def __init__(self, channel_group_manager: IChannelGroupManager,  async_receiver_task_manager: IAsyncReceiverTaskManager) -> None:
        
        intents = nextcord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.guilds = True
        super().__init__(intents=intents)
        
        self._channel_group_manager = channel_group_manager
        self._async_receiver_task_manager = async_receiver_task_manager
    
    async def on_ready(self):        
        print(f'{self.user} has connected to discord!')
    
    def get_channel_group_manager(self) -> IChannelGroupManager:
        return self._channel_group_manager
    
    def get_async_receiver_task_manager(self):
        return self._async_receiver_task_manager