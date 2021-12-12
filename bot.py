import discord
from discord.ext import commands
import requests
from requests.structures import CaseInsensitiveDict
import json
import pycoingecko
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix=">")

#Setting Game
@client.event
async def on_ready ():
    game = discord.Game("with cool nft's")
    #using btc price, defined above to be seen in game activity
    activity = discord.Activity(name='eth price ($ USD)', type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Game, activity=activity)

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

print(initial_extensions)

client.run(os.getenv("BOT_TOKEN"))