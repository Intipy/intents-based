import discord
from discord.ext import commands, tasks


bot = commands.Bot(command_prefix="파이드")



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.command()
async def 안녕(ctx):
    await ctx.send("반갑다 씹년아")

@bot.command()
async def 안녕 하다(ctx):
    await ctx.send("반갑하다 씹년아")

@bot.command()
async def 헬로(ctx):
    await ctx.send("나이스")


m = "NzkwODQ2MTM1MzIxMjMxMzgx"+".X-Gi2w.wd8kpfrRxsrJVKvGISXl8ICgzqU"
client.run(m)
