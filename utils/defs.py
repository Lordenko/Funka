def load_cogs(bot, *initial_extensions):
    for extension in initial_extensions:
        bot.load_extension(extension)