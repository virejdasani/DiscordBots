import discord
from discord.ext import commands
import requests
import os
import urllib.parse
import json

appid_wolfram = "WOLFRAM-DEV-ID"

CONST_prefix = '!'

bot_TOKEN = "DISCORDBOTTOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=CONST_prefix, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms')

@bot.command()
async def population(ctx, arg):

    query = urllib.parse.quote_plus(arg + " Population")
    query_url = f"http://api.wolframalpha.com/v2/query?" \
             f"appid={appid_wolfram}" \
             f"&input={query}" \
             f"&format=plaintext" \
             f"&output=json"

    r = requests.get(query_url).json()        

    await ctx.send(r["queryresult"]["pods"][0]["subpods"][0]["plaintext"] +" is: " + r["queryresult"]["pods"][1]["subpods"][0]["plaintext"])


    
bot.run(bot_TOKEN)