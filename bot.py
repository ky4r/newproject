from discord.ext import commands; import datetime; import asyncio; import time; import requests; import json; import discord; from discord_webhook import DiscordWebhook, DiscordEmbed

TOKEN = "OTA0MzY5MTEwNzk4OTg3MjY0.YX6hXg.V05nW6TfXeRUlBE0vdUmyCamFZI"

commandsissued = 0
eauthors = 'Сын Кеши#5072 / QuantoTeam, 2021'
dt_now = datetime.datetime.now().replace(microsecond=0)
print(dt_now)

bot = commands.Bot(command_prefix=('-='))
bot.remove_command('help')

@bot.event
async def on_ready():
    print("QUANTOBOT {\} Бот успешно запущен")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"https://discord.gg/HvNDFVfH"))

@bot.command()
async def infgenesis(ctx, arg1, arg2):
    global commandsissued
    commandsissued = commandsissued + 1
    if ctx.author.guild_permissions.administrator:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/904424068122562600/sa-mKRUmC4OteMHm9MG6BRuOsNqi9d3HF7VeO2AytRaSR59L3A-bIxQcCsHbDn21JKZe')
        embed = DiscordEmbed(title=arg1, description=arg2, color='567cff')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        await ctx.send('Команда *infgenesis* доступна только администраторам.')

@bot.command()
async def infdarkrp(ctx, arg1, arg2):
    global commandsissued
    commandsissued = commandsissued + 1
    if ctx.author.guild_permissions.administrator:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/904424113664315402/mcJ-0pUaTa7JFaV8g2iVy_UAPO98b61lKV7bubx3bB4ECjxDohaUQXsXgXpKGJoIE62R')
        embed = DiscordEmbed(title=arg1, description=arg2, color='ffffff')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        await ctx.send('Команда *infdarkrp* доступна только администраторам.')

@bot.command(name="mc")
async def member_count(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    a=ctx.guild.member_count
    b=discord.Embed(title=f"Информация о сервере {ctx.guild.name}",description=f"Кол-во участников: {a}",color=discord.Color((0x4d8062)))
    await ctx.send(embed=b)

@bot.command(name='help')
async def help(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    embed = discord.Embed(
        title = 'Помощь по QUANTOBOT',
        description = '''Список команд:''',
        colour = 0x8ea091
    )
    embed.add_field(name="Основные команды", value='''-=mc - доступная информация о сервере
    -=status - состояние бота''', inline=True)
#    embed.add_field(name="Админ-команды", value='''-=infgenesis "Заголовок" "Информация" - изменения в режиме Genesis
#    -=infdarkrp "Заголовок" "Информация" - изменения в режиме DarkRP''', inline=True)
    embed.add_field(name="Random API", value='''-=cat - фото кота
    -=dog - фото собаки
    -=fox - фото лисы
    -=panda - фото панды''', inline=True)
    embed.add_field(name="Игры", value="В разработке...", inline=True)
    embed.set_footer(text=eauthors, icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await ctx.send(embed=embed)

@bot.command(name='ahelp')
async def ahelp(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    embed = discord.Embed(
        title = 'Помощь по QUANTOBOT [ADMIN]',
        description = 'Список команд:',
        colour = 0x8b4049
    )
    embed.add_field(name="Обновления", value='''-=infdarkrp "Заголовок" "Текст" - объявить об изменениях в режиме DarkRP
     -=infgenesis "Заголовок" "Текст" - объявить об изменениях в режиме Genesis''', inline=True)
    embed.set_footer(text=eauthors, icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
    await ctx.send(embed=embed)

@bot.command(name='status')
async def status(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    dt_nows = datetime.datetime.now().replace(microsecond=0)
    embed = discord.Embed(
        title = 'Состояние QUANTOBOT',
        description = f'''**Пинг:** {round(bot.latency * 1000)}ms
**Сеанс начат:** {dt_now}
**Время работы:** {dt_nows - dt_now}
**За данный сеанс команд обработано:** {commandsissued}
**Доступных команд:** 10''',
        colour = 0x515262
    )
    await ctx.send(embed=embed)

@bot.command()
async def fox(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xae6a47)
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def dog(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xae6a47)
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def cat(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xae6a47)
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def panda(ctx):
    global commandsissued
    commandsissued = commandsissued + 1
    response = requests.get('https://some-random-api.ml/img/panda') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xae6a47)
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

bot.run(TOKEN)
