import asyncio
from receiver import *
from broadcaster import *
from nextcord.ext import commands
from abc import ABC, abstractmethod

class IAsyncReceiverTaskManager(ABC):
    
    @abstractmethod
    def add_task():
        pass
    
    @abstractmethod
    def remove_task():
        pass
    
class AsyncReceiverTaskManager(IAsyncReceiverTaskManager):
    
    def __init__(self):
        self._task_list = []
    
    def add_task(self, loop: asyncio.AbstractEventLoop, receiver: IReceiver):
        
        queue_name = receiver.get_queue_name()
        
        exist = False
        for task in self._task_list:
            if task.get_name() == queue_name:
                exist = True
                
        if not exist:
            
            task = loop.create_task(receiver.start(queue_name))
            task.set_name(queue_name)
            
            self._task_list.append(task)
        
    def remove_task(self, queue_name):
        for task in self._task_list:
            if task.get_name() == queue_name:
                self._task_list.remove(task)