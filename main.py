# Discord imports
from discord.ext import commands
import discord, os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")



intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):
        await message.channel.send("You mentioned me?")

    # Help menu
    elif message.content == '!help':
        embed = discord.Embed(
            color = discord.Colour.gold()
        )
        embed.set_author(name="Commands List")
        embed.add_field(name="**!help**", value="Brings up this help page", inline=False)
        await message.channel.send(embed=embed) 
    
    elif message.content == 'ping':
        # "pong" then return IP address
        await message.channel.send("pong!\n")


client.run(TOKEN)
