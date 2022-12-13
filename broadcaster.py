from abc import ABC, abstractmethod
import nextcord
from embed import CustomEmbed
import nextcord

class IBroadcaster(ABC):
    
    @abstractmethod
    def send(self, message: dict):
        pass
    
class Broadcaster(IBroadcaster):
    
    def __init__(self, client) -> None:
        self._client = client
    
    async def send(self, message: dict) -> bool:
        
        channel_group_manager = self._client.get_channel_group_manager()
        has_channel, token = channel_group_manager.has_channel(message["channel_id"])
        channel_groups = channel_group_manager.get_channel_groups()
        
        if has_channel:
        
            for grouped_channel in channel_groups[token]:
                
                channel = self._client.get_channel(grouped_channel)
                
                embed = CustomEmbed.create_embed(message=message)
                
                if message["channel_id"] != grouped_channel:
                    
                    await channel.send(embed=embed)

            return True
        
        else:
            
            return False