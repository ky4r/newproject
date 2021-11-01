import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio
from time import sleep

TOKEN = "OTA0MzcyODEyODU1Mjc5NjQ2.YX6k0Q.qBHMJNJDjISXkpGBp7MpfyVVJp8"

bot = commands.Bot(command_prefix=('-='))
bot.remove_command('help')

@bot.event
async def on_ready():
    print("QUANTOBOT {\} Бот успешно запущен")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"https://discord.gg/HvNDFVfH"))

@bot.command()
async def infgenesis(ctx, arg1, arg2):
    if ctx.author.guild_permissions.administrator:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/904424068122562600/sa-mKRUmC4OteMHm9MG6BRuOsNqi9d3HF7VeO2AytRaSR59L3A-bIxQcCsHbDn21JKZe')
        embed = DiscordEmbed(title=arg1, description=arg2, color='567cff')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        await ctx.send('Команда *infgenesis* доступна только администраторам.')

@bot.command()
async def infdarkrp(ctx, arg1, arg2):
    if ctx.author.guild_permissions.administrator:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/904424113664315402/mcJ-0pUaTa7JFaV8g2iVy_UAPO98b61lKV7bubx3bB4ECjxDohaUQXsXgXpKGJoIE62R')
        embed = DiscordEmbed(title=arg1, description=arg2, color='ffffff')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        await ctx.send('Команда *infdarkrp* доступна только администраторам.')

@bot.command(name="понг")
async def ping(ctx: commands.Context):
    await ctx.send(f"Пинг бота: {round(bot.latency * 1000)}ms")

@bot.command(name="mc")
async def member_count(ctx):
    a=ctx.guild.member_count
    b=discord.Embed(title=f"Информация о сервере {ctx.guild.name}",description=f"Кол-во участников: {a}",color=discord.Color((0x4d8062)))
    await ctx.send(embed=b)

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title = 'Помощь по QUANTOBOT',
        description = '''Список команд:''',
        colour = 0x9068a3
    )
    embed.add_field(name="Основные команды", value='''-=mc - доступная информация о сервере
    -=понг - пинг бота''', inline=True)
    embed.add_field(name="Админ-команды", value='''-=infgenesis "Заголовок" "Информация" - изменения в режиме Genesis
    -=infdarkrp "Заголовок" "Информация" - изменения в режиме DarkRP''', inline=True)
    embed.add_field(name="Игры", value="В разработке...", inline=False)
    embed.set_footer(text="Сын Кеши#5072 / QuantoTeam, 2021", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await ctx.send(embed=embed)

bot.run(TOKEN)
