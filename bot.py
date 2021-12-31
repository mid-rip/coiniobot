import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ui import Button
import requests
from requests.structures import CaseInsensitiveDict
import json
import pycoingecko
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import os
from dotenv import load_dotenv
import asyncio



load_dotenv()

client = commands.Bot(command_prefix=">")

debug_guild = "879345472815386674"
owner_id = "230150255742681091"

btcprice = cg.get_coin_by_id("bitcoin")
client.remove_command("help")

#Setting Game
@client.event
async def on_ready ():
    game = discord.Game("with cool nft's")
   #using btc price, defined above to be seen in game activity
    activity = discord.Activity(name='btc price ($%s USD)' % btcprice, type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Game, activity=activity)


##Custom Help Command
#@client.group(invoke_without_command=True)
#async def help(ctx):
#    embed = discord.Embed(title = "Coinio Help Page", description = "Use c.help [command] for more information and proper syntax", color=0x8652ff)
#    embed.add_field(name = "Information Commands", value = "Trending, Defi")
#    embed.add_field(name = "Crypto Utility", value = "Coin, Chart")
#    embed.set_footer(text="Coinio, The best crypto info client ever!")
#
#    await ctx.send(embed=embed)

#@help.command()
#async def kick

page1 = discord.Embed(title="client Help 1", description="Use the buttons below to navigate between help pages.", colour=discord.Colour.orange())
page2 = discord.Embed(title="client Help 2", description="Page 2", colour=discord.Colour.orange())
page3 = discord.Embed(title="client Help 3", description="Page 3", colour=discord.Colour.orange())
page4 = discord.Embed(title="DELETED", description="Page 3", colour=discord.Colour.orange())
client.help_pages = [page1, page2, page3, page4]



#@client.command()
#async def help(ctx):
#    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
#    current = 0
#    msg = await ctx.send(embed=client.help_pages[current])
#    
#    for button in buttons:
#        await msg.add_reaction(button)
#        
#    while True:
#        try:
#            reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)
#
#        except asyncio.TimeoutError:
#            return print("test")
#
#        else:
#            previous_page = current
#            if reaction.emoji == u"\u23EA":
#                current = 0
#                
#            elif reaction.emoji == u"\u2B05":
#                if current > 0:
#                    current -= 1
#                    
#            elif reaction.emoji == u"\u27A1":
#                if current < len(client.help_pages)-1:
#                    current += 1
#
#            elif reaction.emoji == u"\u23E9":
#                current = len(client.help_pages)-1
#            
#
#            for button in buttons:
#                await msg.remove_reaction(button, ctx.author)
#
#            if current != previous_page:
#                await msg.edit(embed=client.help_pages[current])



initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

print(initial_extensions)

client.run(INSERT TOKEN)
