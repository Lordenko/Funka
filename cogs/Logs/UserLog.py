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
        
        # actions in same channel
        if (after.channel and before.channel) and after.channel == before.channel:
            
            #
            # mute/deaf
            #

            if after.self_deaf:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has deaf by self') ]
                )
                await embed.create_embed()

            elif after.self_mute:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has muted by self') ]
                )
                await embed.create_embed()
            
            elif after.deaf:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has deaf by server') ]
                )
                await embed.create_embed()

            elif after.mute:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has muted by server') ]
                )
                await embed.create_embed()
            
            #
            # unmute/undeaf
            #

            if before.self_deaf and not after.self_deaf:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has undeaf by self') ]
                )
                await embed.create_embed()

            elif before.self_mute and not after.self_mute:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has unmuted by self') ]
                )
                await embed.create_embed()
            
            elif before.deaf and not after.deaf:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has undeaf by server') ]
                )
                await embed.create_embed()

            elif before.mute and not after.mute:
                embed = CustomEmbed(
                    channel = self.bot.get_channel(self.voice_channel_id),
                    color = member.roles[-1].colour,
                    author_name = member.display_name,
                    author_icon_url = member.display_avatar,
                    fields = [ Embed_Field(value=f'{member.mention} has unmuted by server') ]
                )
                await embed.create_embed()
            

        # action in new channel
        elif after.channel:
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

        # disconnect action
        elif before.channel and after.channel is None:
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
                
                #
                # Message link
                # https://discord.com/channels/guild_id/chat_id/message_id
                #

                fields = [
                    Embed_Field(value=f'Message https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id} by {before.author.mention} has edited!\n```Before: {before.content}\n\nAfter: {after.content}```')
                ]
            )
        await embed.create_embed()



def setup(bot):
    bot.add_cog(UserLog(bot))
