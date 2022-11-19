from abc import ABC, abstractmethod
import discord
from group import IGroup
from embed import CustomEmbed
import discord

class IBroadcaster(ABC):
    
    @abstractmethod
    def send(self, message: dict):
        pass
    
class Broadcaster(IBroadcaster):
    
    def __init__(self, client: discord.Client, group: IGroup) -> None:
        self._client = client
        self._group = group
    
    async def send(self, message: dict) -> bool:
        
        group: list = self._group.get_list()
        
        if message["channel_id"] in group:
            
            for grouped_channel in group:
                
                channel = self._client.get_channel(grouped_channel)
                # if(message["channel_id"] == channel.id):
                #     m = await channel.fetch_message(message["message_id"])
                #     await m.delete()
                
                embed = CustomEmbed.create_embed(message=message)
                
                if message["channel_id"] != grouped_channel:
                    
                    await channel.send(embed=embed)
                
                else:
                    pass
                    # await channel.send(message["mentions"], embed=embed)
            
            return True
        
        else:
            
            print(message)
            
            return False