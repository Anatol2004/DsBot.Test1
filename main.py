from encodings.aliases import aliases
import functions


# Функция включения бота-------------------
@functions.bot.event
async def on_ready():
    print(f"{functions.bot.user} готов к работе.")


functions.bot.run("MTMzNjI1MzcwOTY0MTg0Mjc2MA.G_OBDu.ebyHxyIXJ-bQgIeNBDvZ9TNzTEq2L0nPnXB2cE")
