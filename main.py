import os
from dotenv import load_dotenv
import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"logado como {client.user}!")
    

guilds_group = {"test": [1042960126837006366, 1042960076304031876]}    

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    message_cache = {"user": f"{message.author.name}#{message.author.discriminator}",
                     "guild": f"From {message.guild.name}",
                     "content": f"```{message.content}```",
                     "color": int(message.author.discriminator)}
    
    if message.channel.name == "geral":
        await message.delete()
        
        for general_channel in guilds_group["test"]:
            channel = client.get_channel(general_channel)
            embedVar = discord.Embed(title= message_cache["user"],
                                    description=message_cache["guild"],
                                    color=message_cache["color"])
            
            embedVar.add_field(name="ㅤ", value=message_cache["content"], inline=False)
            
            await channel.send(embed=embedVar)

if __name__ == "__main__":
    load_dotenv()
    client.run(os.getenv('TOKEN'))