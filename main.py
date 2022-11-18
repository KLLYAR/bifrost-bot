import os
from dotenv import load_dotenv
import discord

from group import Group
from broadcaster import Broadcaster
from message import Message

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"logado como {client.user}!")

ads_group = Group()
ads_group.add_channel(1042960126837006366)
ads_group.add_channel(1042960076304031876)

ads_broadcaster = Broadcaster(client, ads_group)

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if(await ads_broadcaster.send(Message(message))): 
        await message.delete() # Slow
    
if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv('TOKEN'))