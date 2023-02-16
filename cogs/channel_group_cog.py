from nextcord import Interaction, Embed, SlashOption
from nextcord.ext import commands
import nextcord
from broadcaster import Broadcaster
from receiver import Receiver
from sender import *
from channel_group_manager import * 
import json
from message_formatter import MessageFormatter as MS
from client import BotClient
from typing import Optional
import secrets
import requests

class ChannelGroupCog(commands.Cog):
    
    def __init__(self, client: BotClient):
        self.client = client
        
        
    @nextcord.slash_command(name="list")
    async def list_public_groups(self, interaction: Interaction) -> None:    
        request = requests.get("http://127.0.0.1:8000/group/")
        
        if request.status_code == 200:
            
            await interaction.response.send_message({"message": request.text}, ephemeral=True)
    
    @nextcord.slash_command(name="register")
    async def register_group(self, interaction: Interaction, name: str, description: str) -> None:
        
        
        request = requests.post("http://127.0.0.1:8000/group/", 
                                {"name": name,
                                 "description": description,
                                 "user_id": interaction.user.id,
                                 "is_owner": 1,
                                 "channel_id": interaction.channel.id})
        
        print(request.text)
        print(request.status_code)
        response_data = request.json()
        
        if request.status_code == 201:
            
            token = response_data["token"]
            
            self.client.get_async_receiver_task_manager().add_task(
                self.client.loop, 
                Receiver(token, Broadcaster(self.client)))
            
            self.client.get_channel_group_manager().add_channel(
                token, 
                interaction.channel.id)
        
            await interaction.response.send_message(f"Group created!. Your group token is {token}", ephemeral=True)

        
        elif request.status_code == 400:
            
            await interaction.response.send_message(response_data["message"], ephemeral=True)
        
        else:
            
            await interaction.response.send_message(response_data["message"], ephemeral=True)
        
    
    @nextcord.slash_command(name="enter")
    async def enter(self, interaction: Interaction, token: str):
        # Check if the passed token exist within a group in database.
        # If not, return a error message. If yes, add_channel()
                
        channel_group_manager = self.client.get_channel_group_manager()

        if channel_group_manager.has_group(token):
            
            has_channel, returned_token = channel_group_manager.has_channel(interaction.channel.id)
            if has_channel:
                
                await interaction.response.send_message(f"This channel already in {returned_token} group", ephemeral=True)
            
                return
            
            self.client.get_channel_group_manager().add_channel(
                token, 
                interaction.channel.id
            )
            
            await interaction.response.send_message(f"Entered in {token} group", ephemeral=True)
            
        else:
            
            await interaction.response.send_message(f"This {token} group does not exist",  ephemeral=True) 
    
    @nextcord.slash_command(name="cancel")
    async def cancel(self, interaction: Interaction) -> None:
        # Get Group
        # Update is_active to false
        # If the owner use /register at the same channel, a same token will be generated and is_active is set to true again
        pass
    
    async def join(self, interaction: Interaction) -> None:
        # Get User_Group
        # Update is_active to true
        pass
    
    async def leave(self, interaction: Interaction) -> None:
        # Get User_Group
        # Update is_active to false
        pass
    
def setup(client):
    client.add_cog(ChannelGroupCog(client))