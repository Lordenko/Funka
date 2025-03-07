from disnake.ext import commands

class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        channel = message.guild.system_channel
        if channel:
            await channel.send(f'{message.content}')

def setup(bot):
    bot.add_cog(EventsCog(bot))
