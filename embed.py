import nextcord

class CustomEmbed():

    def create_embed(message):
        embed = nextcord.Embed(
            title=message["username"],
            description=message["guild"],
            color=message["color"])
                
        embed.set_thumbnail(url=message["user_avatar"])
        
        embed.add_field(name="ㅤ", value=message["content"], inline=False)
        
        embed.set_footer(text=message["date"])
        
        return embed