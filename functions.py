import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!pbot1", help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[1335883550804934760])

CENSORED_WORDS = ["apple", "bye", "amogus"]


# Event функции
# region Функция подключения нового участника на сервер
@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1339661075682951239)
    channel = member.guild.system_channel

    embed = disnake.Embed(
        title="Новый участник!",
        description=f"{member.name}",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


# endregion
# region Функция фильтрации сообщений
@bot.event
async def on_message(message):
    await bot.process_commands(message)

    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content.lower() == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} такие слова запрещены.")


# endregion
# region Функция обработок ошибок
@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполнения данной команды.")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Правильное использование команды: '{ctx.prefix}{ctx.command.name}' ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))


# endregion

# Сommand функции
# region Функция команды "kick"
@bot.command(brief="кик", usage="tb1kick <@user> <причина>")
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Нарушение правил."):
    await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}", delete_after=60)
    await member.kick(reason=reason)
    await ctx.message.delete()


# endregion
# region Функция команды "ban"
@bot.command(name="ban")
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason="Нарушение правил."):
    await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}", delete_after=60)
    await member.ban(reason=reason)
    await ctx.message.delete()


# endregion
# region Функция слэш-команды "calculator" (Плохо работает)
@bot.slash_command(description="Простой калькулятор.")
async def calculator(inter, a: int, oper: str, b: int):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    else:
        result = "Неверный оператор."

    await inter.send(str(result))
# endregion
