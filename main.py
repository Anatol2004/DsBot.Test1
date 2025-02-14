from encodings.aliases import aliases
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="tb1", help_command=None, intents=disnake.Intents.all())

CENSORED_WORDS = ["apple", "bye", "amogus"]


@bot.event  # Функция включения бота----------
async def on_ready():
    print(f"{bot.user} готов к работе.")


@bot.event  # Функция захода на сервер участника-----------------------------
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1335883551916429373)
    channel = member.guild.system_channel

    embed = disnake.Embed(
        title="Новый участник!",
        description=f"{member.name}",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event  # Функция фильтрации слова -------------------------------------------------------------------------
async def on_message(message):
    await bot.process_commands(message)

    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content.lower() == censored_word:
                await message.delete()
                await message.channel.send(f"{message.author.mention} это запрещённое слово.", delete_after=10)


# Функция кика-------------------------------------------------------------------------------------
@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Нарушение правил."):
    await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}",
                   delete_after=60)
    await member.kick(reason=reason)
    await ctx.message.delete()


# Функция бана ---------------------------------------------------------------------------------
@bot.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason="Нарушение правил."):
    await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя {member.mention}",
                   delete_after=60)
    await member.ban(reason=reason)
    await ctx.message.delete()


# Функция вывода ошибки
@bot.event()
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}")


bot.run("MTMzNjI1MzcwOTY0MTg0Mjc2MA.G_OBDu.ebyHxyIXJ-bQgIeNBDvZ9TNzTEq2L0nPnXB2cE")
