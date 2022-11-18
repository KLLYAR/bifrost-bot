from abc import ABC, abstractmethod

class IMessage(ABC):
    pass
    
class Message(IMessage):
    
    def __init__(self, data):
        self.username = f"__{data.author.name}#{data.author.discriminator}__"
        self.guild = f"*From {data.guild.name}*"
        self.content = f"```{data.content}```"
        self.color = int(f"{ord(data.author.name[0])}{data.author.discriminator}")
        self.channel_id = data.channel.id