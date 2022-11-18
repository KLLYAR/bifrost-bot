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
            
            for grouped_channel in group:
                
                channel = self._client.get_channel(grouped_channel)
                
                embed = discord.Embed(title=message.username,
                                        description=message.guild,
                                        color=message.color)
                
                embed.set_thumbnail(url=message.user_avatar)
                
                embed.add_field(name="ㅤ", value=message.content, inline=False)
                
                embed.set_footer(text=message.data)
                
                if message.channel_id != grouped_channel:
                    
                    await channel.send(embed=embed)
                
                else:
                
                    await channel.send(message.mentions, embed=embed)
            
            return True
        
        else:
            
            print(message)
            
            return False