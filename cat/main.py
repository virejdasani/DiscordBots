import discord
from discord import app_commands
import typing 
import requests

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


bot_TOKEN = "token"

@bot.event
async def on_ready():
    await tree.sync()
    print("Ready!")


@tree.command(name = "cat", description = "Gives cat pictures") 
async def cat(interaction: discord.Interaction, tag: typing.Optional[str]):
    if tag == None:
        # no tags
        await interaction.response.send_message("https://cataas.com"+get_url("null"))
    else:
        # tags
        await interaction.response.send_message("https://cataas.com"+get_url(tag))

@tree.command(name = "src_cats", description = "Gives api link where the cat pictures are retrieved.") 
async def src_cats(interaction):
    await interaction.response.send_message("The api used to get all the cat pictures, is https://cataas.com/")

def get_url(tag):
    x = "initiate"
    if tag == "null":
        x = requests.get("https://cataas.com/cat?json=true").json()
    else:
        x = requests.get(f"https://cataas.com/cat/{tag}?json=true").json()

    return x["url"]

    
bot.run(bot_TOKEN)