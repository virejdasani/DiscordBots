import discord
from discord.ext import commands

PREFIX = '!'
KMTOMI = 0.62137
MITOKM = 1.60934

TOKEN = "BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.command()
async def kmtomiles(ctx, num):
    await ctx.send(round(KMTOMI*num, 5))

@bot.command()
async def milestokm(ctx, num):
    await ctx.send(round(MITOKM*num, 5))


bot.run(TOKEN)
