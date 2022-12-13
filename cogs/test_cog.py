from nextcord import Interaction, Embed
from nextcord.ext import commands
import nextcord

class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @nextcord.slash_command(name="ping")
    async def ping(self, interaction: Interaction) -> None:
        ping1 = f"{str(round(self.client.latency * 1000))} ms"
        embed = Embed(title = "**Pong!**", description = "**" + ping1 + "**", color = 0xafdafc)
        await interaction.response.send_message(embed = embed)
        
def setup(client):
    client.add_cog(TestCog(client))