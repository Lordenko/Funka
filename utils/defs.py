def load_cogs(bot, *initial_extensions):
    for extension in initial_extensions:
        bot.load_extension(extension)

async def vc_disconnect(vc):
    asyncio.sleep(3)
    await vc.disconnect()