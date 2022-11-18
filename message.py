from abc import ABC, abstractmethod
from datetime import datetime

class IMessage(ABC):
    pass
    
class Message(IMessage):
    
    def __init__(self, data):
        self.user_id = int(data.author.id)
        self.username = f"__{data.author.name}#{data.author.discriminator}__"
        self.guild = f"*From **{data.guild.name}** | {data.channel.name}*"
        self.content = f"```{data.clean_content}```"
        self.color = int(f"{self._sum_chars(data.author.name)}{data.author.discriminator}")
        self.channel_id = data.channel.id
        self.mentions = self._get_mentions(data.mentions)
        self.user_avatar = data.author.avatar.url
        self.data = datetime.now().strftime("%d/%m/%Y | %H:%M")
        
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