import asyncio

from disnake.ext import commands
import disnake
from disnake import FFmpegPCMAudio

from datetime import datetime, timedelta

from utils.defs import knight_say

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.history = {}

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.id == 366581917522591744:
            if not before.mute and after.mute:
                print(f"{member.display_name} був зам'ючений")
                await member.edit(mute=False)

            if not before.deaf and after.deaf:
                print(f"{member.display_name} був заглушений")
                await member.edit(deafen=False)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        message = f'Ласкаво просимо, {member.mention}!\n'
        no_bot_message = 'Тобі потрібно вибрати свою групу в <#1174023100392808478>'
        message = message+no_bot_message if not member.bot else message

        if channel:
            await channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'{member.mention} покинув нас. Сумуватимемо!')

    @commands.Cog.listener()
    async def on_message(self, message):
        connect_to_voice = True

        await knight_say(
            message=message,
            history=self.history,
            say='иди нахуй',
            path_to_file='media/извинись.ogg',
            bot = self.bot,
            connect_to_voice=connect_to_voice
        )

        await knight_say(
            message=message,
            history=self.history,
            say='женщина',
            path_to_file='media/женщина.ogg',
            bot = self.bot,
            connect_to_voice=connect_to_voice
        )

        await knight_say(
            message=message,
            history=self.history,
            say='нет',
            path_to_file='media/нет.ogg',
            bot = self.bot,
            connect_to_voice=connect_to_voice
        )



def setup(bot):
    bot.add_cog(EventsCog(bot))
