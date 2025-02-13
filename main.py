import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix = "!pbot1", help_command = None, intents = disnake.Intents.all())


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

bot.run("MTMzNjI1MzcwOTY0MTg0Mjc2MA.G_OBDu.ebyHxyIXJ-bQgIeNBDvZ9TNzTEq2L0nPnXB2cE")