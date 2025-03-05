import disnake
from disnake.ext import commands
import json
import asyncio

from utils.defs import load_cogs
from data.config import token

intents = disnake.Intents.all()

bot = commands.InteractionBot(intents=intents)
load_cogs(bot, 'cogs.commands', 'cogs.events')

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

    activities = [
        disnake.Activity(type=disnake.ActivityType.watching, name="to broken code."),
        disnake.Activity(type=disnake.ActivityType.watching, name="to broken code.."),
        disnake.Activity(type=disnake.ActivityType.watching, name="to broken code..."),
        disnake.Activity(type=disnake.ActivityType.watching, name="to broken code.."),

    ]

    while True:
        for activity in activities:
            await bot.change_presence(activity=activity)
            await asyncio.sleep(2)


bot.run(token)
