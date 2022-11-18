from abc import ABC, abstractmethod
import discord
from message import IMessage
from group import IGroup

class IBroadcaster(ABC):
    
    @abstractmethod
    def send(self, message: IMessage):
        pass
    
class Broadcaster(IBroadcaster):
    
    def __init__(self, client, group: IGroup) -> None:
        self._client = client
        self._group = group
    
    async def send(self, message: IMessage) -> bool:
        
        group: list = self._group.get_list()
        if message.channel_id in group:
            # await message.delete()
            
            for grouped_channel in group:
                
                channel = self._client.get_channel(grouped_channel)
                
                embed = discord.Embed(title=message.username,
                                        description=message.guild,
                                        color=message.color)
                
                embed.add_field(name="ㅤ", value=message.content, inline=False)
                
                await channel.send(embed=embed)
            
            return True
        
        else:
            
            print(message)
            
            return False