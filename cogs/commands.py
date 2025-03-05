import disnake
from disnake.ext import commands

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="hello", description="Додає два числа")
    async def hello(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message('Дарова')

def setup(bot):
    bot.add_cog(CommandsCog(bot))
