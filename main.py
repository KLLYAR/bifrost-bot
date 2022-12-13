import os
from dotenv import load_dotenv

from client import *
from sender import *
from channel_group_manager import *

if __name__ == "__main__":
    load_dotenv()
    
    initial_extensions = []
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            initial_extensions.append("cogs." + filename[:-3])

    client = BotClient(ChannelGroupManager(), AsyncReceiverTaskManager())

    for extension in initial_extensions:
        print(extension)
        client.load_extension(extension)        
    
    client.run(os.getenv('TOKEN'))