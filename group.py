from abc import ABC, abstractmethod

class IGroup(ABC):
    
    @abstractmethod
    def get_list(self):
        pass

class Group(IGroup):

    def __init__(self):
        self._token = self._generate_token()
        self._channel_list = []
    
    def add_channel(self, channel_id: int):
        self._channel_list.append(channel_id)
        
    def remove_channel(self, channel_id: int):
        self._channel_list.remove(channel_id)
    
    def get_list(self) -> list:
        return self._channel_list
    
    def _generate_token(self) -> str:
        return "123"