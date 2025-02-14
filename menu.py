import disnake
from disnake import MessageInteraction
from disnake.ext import commands
from disnake.ui.item import ClientT

bot = commands.Bot(command_prefix=commands.when_mentioned, help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[1335883550804934760])


# region Функция включения бота
@bot.event
async def on_ready():
    print(f"{bot.user} готов к работе (menu).")


# endregion

class DropDown(disnake.ui.StringSelect):

    def __init__(self):
        options = [
            disnake.SelectOption(label="Burger", description="Очень вкусный."),
            disnake.SelectOption(label="Voda", description="Чтоб утолить жажду."),
            disnake.SelectOption(label="Кола", description="Сладкая газировка.")
        ]

        super().__init__(
            placeholder="Menu",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.send_message(f"Вы заказали {self.values[0]}. Ожидайте доставки.")


class DropdownView(disnake.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(DropDown())


@bot.command()
async def order(ctx):
    await ctx.send("Выберите, что желаете заказать:", view=DropdownView())


bot.run("MTMzNjI1MzcwOTY0MTg0Mjc2MA.G_OBDu.ebyHxyIXJ-bQgIeNBDvZ9TNzTEq2L0nPnXB2cE")
