import discord
from discord.ext import commands

CONST_prefix = '!'

bot_TOKEN = "BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=CONST_prefix, intents=intents)

@bot.command()
async def kmtomiles(ctx, arg):
	await ctx.send(round(0.62137119*float(arg)/1.00, 5))

@bot.command()
async def milestokm(ctx, arg):
	await ctx.send(round(1.60934*float(arg)/0.9999975145, 5))



    
bot.run(bot_TOKEN)