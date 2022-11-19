from abc import ABC, abstractmethod
from datetime import datetime
import json

class IMessage(ABC):
    pass
    
class Message(IMessage):
    
    def __init__(self, message) -> None:
        self._data: json = {
            "message_id": message.id,
            "user_id": message.author.id,
            "username": f"__{message.author.name}#{message.author.discriminator}__",
            "guild": f"*From **{message.guild.name}** | {message.channel.name}*",
            "content": f"```{message.clean_content}```",
            "color": int(f"{self._sum_chars(message.author.name)}{message.author.discriminator}"),
            "channel_id": message.channel.id,
            "mentions": self._get_mentions(message.mentions),
            "user_avatar": message.author.avatar.url,
            "date": datetime.now().strftime("%d/%m/%Y | %H:%M:%S"),
        } 
        
    def get_data(self) -> json:
        return self._data
        
    def _get_mentions(self, mentions: list) -> str:
        formatted_mentions = ""
        
        for member in mentions:
            formatted_mentions += f"||<@{member.id}>||"
            
        return formatted_mentions
    
    def _sum_chars(self, array: list) -> int:
        sum = 0
        
        for i in array:
            sum += ord(i)
        
        return sum