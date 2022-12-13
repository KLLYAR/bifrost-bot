from abc import ABC, abstractmethod

class IChannelGroupManager(ABC):
    
    @abstractmethod
    def get_channel_groups(self):
        pass

class ChannelGroupManager(IChannelGroupManager):

    def __init__(self):
        self._grouped_channels = {}
    
    def add_channel(self, token: str, channel_id: int):
        self._add_group_if_not_exist(token)
        self._grouped_channels[token].append(channel_id)
    
    def remove_channel(self, token: str, channel_id: int):
        if token in self._grouped_channels:
            if channel_id in self._grouped_channels[token]:
                self._grouped_channels[token].remove(channel_id)
    
    def _add_group_if_not_exist(self, token: str):
        if token not in self._grouped_channels:
            self._grouped_channels[token] = []
        
    def remove_group(self, token: str):
        if token in self._grouped_channels:
            self._grouped_channels.pop(token)
    
    def has_channel(self, channel_id: int) -> tuple:
        for token in self._grouped_channels:
            
            if channel_id in self._grouped_channels[token]:
                return (True, token)
        
        return (False, "")
    
    def has_group(self, token: str):
        if token in self._grouped_channels:
            
            return True
        
        return False
        
    def get_channel_groups(self) -> dict:
        return self._grouped_channels