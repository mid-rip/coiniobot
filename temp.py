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

#https://stackoverflow.com/questions/58700380/in-python-how-do-i-get-specific-fields-from-json-response
#^^ Useful Link for parsing json data

"""
BEGIN PRICE FIND
"""

price_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Ccardano%2Cbinancecoin%2Cripple%2Ctether%2Csolana%2Cdogecoin&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false"

headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"


resp = requests.get(price_url, headers=headers)
data = resp.json()

ethprice = data['ethereum']['usd']
btcprice = data['bitcoin']['usd']
xrpprice = data['ripple']['usd']
#Print btc price to console (Testing the api request)
print('Bitcoin is trading at %s $USD' % btcprice)
print('Ripple is trading at %s $USD' % xrpprice)




client = commands.Bot(command_prefix=">")


#Setting Game
@client.event
async def on_ready ():
    game = discord.Game("with cool nft's")
    #using btc price, defined above to be seen in game activity
    activity = discord.Activity(name='eth price ($%s USD)' % ethprice, type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Game, activity=activity)


@client.command()
async def ping(ctx):
    await ctx.send("pong")
    #Test command to see if working

@client.command()
async def btc(ctx):
    await ctx.send("The current BTC price is %s USD" % (btcprice))
    #Same as on_ready except in cmd format
@client.command()
async def eth(ctx):
    await ctx.send("The current ETH price is %s USD" % (ethprice))

@client.command()
async def em(ctx):

    social_url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    # API url to trending searches
    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"


    resp = requests.get(social_url, headers=headers)
    sdata = resp.json()

    print(sdata['description']['en'])
    # ^^Full json object recieved from API call
    trend1 = (sdata['coins'][0]['item']['id'])
    trend2 = (sdata['coins'][1]['item']['id'])
    trend3 = (sdata['coins'][2]['item']['id'])
    # Finding the top 3 trending coins id's (btc, eth) and assigning to vars

    t1 = cg.get_price(ids=[trend1, trend2, trend3], vs_currencies=['usd'], include_24hr_change='true')
    #                       ^Getting prices of trending coins using symbols from api call above
    embed=discord.Embed(title="Trending Coins", url="https://www.beemo.best", description="Highest searched coins on coingecko", color=0x8b3dff)
    embed.add_field(name=trend1, value="%s" % t1[trend1]['usd'], inline=True)
    embed.add_field(name=trend2, value="%s" % t1[trend2]['usd'], inline=True)
    embed.add_field(name=trend3, value="%s" % t1[trend3]['usd'], inline=True)
    await ctx.send(embed=embed)
    #embed


client.run(os.getenv("BOT_TOKEN"))