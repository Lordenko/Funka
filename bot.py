import disnake
from disnake.ext import commands

import json
import asyncio
import os

from datetime import datetime

from utils.defs import load_cogs
from data.config import token

# Permissions
intents = disnake.Intents.all()

bot = commands.InteractionBot(intents=intents)

# Load cogs
for folder in ['GeneralCommands', 'GeneralEvents', 'Logs']:
    for file in os.listdir(f"cogs/{folder}"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{folder}.{file[:-3]}")

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="to broken code..."))

bot.run(token)
