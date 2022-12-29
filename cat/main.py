import discord
from discord.ext import commands
import requests
CONST_prefix = '!'

bot_TOKEN = "token"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=CONST_prefix, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms')

@bot.command()
async def src_cats(ctx):
    await ctx.send("The api used to get all the cat pictures, is https://cataas.com/")

@bot.command()
async def cat(ctx, *args):
    arguments = ', '.join(args)
    if len(arguments) == 0:
        # no tags
        await ctx.send("https://cataas.com"+get_url("null"))
    else:
        # tags
        await ctx.send("https://cataas.com"+get_url(arguments))
# gETTING URL
def get_url(tag):
    x = "initiate"
    if tag == "null":
        x = requests.get("https://cataas.com/cat?json=true").json()
    else:
        x = requests.get(f"https://cataas.com/cat/{tag}?json=true").json()

    return x["url"]

    
bot.run(bot_TOKEN)