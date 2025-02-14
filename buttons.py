from typing import Optional

import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[1335883550804934760])


# region Функция включения бота
@bot.event
async def on_ready():
    print(f"{bot.user} готов к работе (buttons).")


# endregion


# region Кнопки вечеринки
class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10.0)
        self.value = Optional[bool]

    @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.green)
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message("Жди ссылку.")
        self.value = True
        self.stop()

    @disnake.ui.button(label="Confirm", style=disnake.ButtonStyle.red)
    async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message("Как хочешь...")
        self.value = False
        self.stop()


# endregion
# region Кнопка входа
class LinkleParty(disnake.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(disnake.ui.Button(label="Join to us!", url="https://www.youtube.com/"))


# endregion
# region Функция команды о привлечения на вечеринку
@bot.command(name="party")
async def ask_party(ctx):
    view = Confirm()

    await ctx.send("Приглашение на вечеринку, согласны ли вы принять в нём участие?", view=view)
    await view.wait()

    if not view.value is None:
        await ctx.send("Ну ладно...")
    elif view.value:
        await ctx.send("Отлично, держите вашу ссылку.", view=LinkleParty)
    else:
        await ctx.send("Вы ничего не получили.")


# endregion

bot.run("MTMzNjI1MzcwOTY0MTg0Mjc2MA.G_OBDu.ebyHxyIXJ-bQgIeNBDvZ9TNzTEq2L0nPnXB2cE")
