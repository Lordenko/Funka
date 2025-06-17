import disnake
from disnake.ext import commands
from utils.create_embed import Embed_Field, CustomEmbed
import datetime

class UserLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_channel_id = 1384325749686796369
        self.message_channel_id = 1384331715899555922


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel:
            embed = CustomEmbed(
                channel = self.bot.get_channel(self.voice_channel_id),
                color = member.roles[-1].colour,
                author_name = member.display_name,
                author_icon_url = member.display_avatar,
                
                fields = [
                    Embed_Field(value=f'{member.mention} has joined to {after.channel.mention}')
                ]

            )
            await embed.create_embed()

        if before.channel and after.channel is None:
            embed = CustomEmbed(
                channel = self.bot.get_channel(self.voice_channel_id),
                color = member.roles[-1].colour,
                author_name = member.display_name,
                author_icon_url = member.display_avatar,
                
                fields = [
                    Embed_Field(value=f'{member.mention} has disconnected from {before.channel.mention}')
                ]

            )
            await embed.create_embed()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = CustomEmbed(
                channel = self.bot.get_channel(self.message_channel_id),
                color = message.author.roles[-1].colour,
                author_name = message.author.display_name,
                author_icon_url = message.author.display_avatar,
                
                fields = [
                    Embed_Field(value=f'Message by {message.author.mention} in {message.channel.mention} has deleted!\n```{message.content}```')
                ]

            )

        await embed.create_embed()


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        embed = CustomEmbed(
                channel = self.bot.get_channel(self.message_channel_id),
                color = before.author.roles[-1].colour,
                author_name = before.author.display_name,
                author_icon_url = before.author.display_avatar,
                
                fields = [
                    Embed_Field(value=f'Message by {before.author.mention} in {before.channel.mention} has edited!\n```{before.content}```\n```{after.content}```')
                ]

            )

        await embed.create_embed()



def setup(bot):
    bot.add_cog(UserLog(bot))
