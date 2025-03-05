import disnake
from disnake.ext import commands
import json

from utils.defs import load_cogs
from data.config import token

intents = disnake.Intents.all()

bot = commands.InteractionBot(intents=intents)

load_cogs(bot, 'cogs.commands', 'cogs.events')

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

bot.run(token)
