import asyncio

from disnake.ext import commands
import disnake
from disnake import FFmpegPCMAudio

from datetime import datetime, timedelta

from utils.defs import vc_disconnect

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.history = {}


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
        if message.author.bot:
            return

        voice = disnake.File('media/извинись.ogg')

        if 'иди нахуй' in message.content.lower():
            now = datetime.now()

            if message.author.id in self.history and now - self.history[message.author.id] < timedelta(minutes=5):
                await message.reply(f'Спробуй через декілька хвилин :)')

            self.history[message.author.id] = now

            if message.author.voice and message.author.voice.channel:
                vc = await message.author.voice.channel.connect()

                media = FFmpegPCMAudio('media/извинись.ogg')
                vc.play(media, after=lambda _: self.bot.loop.create_task(vc_disconnect(vc)))
            else:
                await message.reply(file=voice)


def setup(bot):
    bot.add_cog(EventsCog(bot))
