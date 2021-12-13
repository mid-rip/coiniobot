from discord.ext import commands
import discord
import requests
from requests.structures import CaseInsensitiveDict
import json
import pycoingecko
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import os
from dotenv import load_dotenv
class Chart(commands.Cog):
    """The description for Coin goes here."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="chart")
    async def chart(self, ctx, arg1, arg2):
        coin = cg.get_coin_by_id(arg1)
        #thumb = (coin['image']['large'])
        symbol = (coin['symbol'])
        chart_thumb = ("https://api.chart-img.com/v1/tradingview/advanced-chart?symbol=%sUSD&width=800&height=400&interval=%s&theme=dark&studies=rsi" % (symbol, arg2))
        name = (coin['name'])
        coinsite = (coin['links']['homepage'][0])
        genesis = (coin['genesis_date'])
        usd_price = (coin['market_data']['current_price']['usd'])
        usd_price_change_24h = (coin['market_data']['price_change_24h'])       
        total_supply = (coin['market_data']['total_supply'])  
        circulating_supply = (coin['market_data']['circulating_supply'])
        last_updated = (coin['market_data']['last_updated'])


        embed=discord.Embed(title=name, url=coinsite, description="Genesis block:", color=0x8652ff)
        embed.add_field(name="Circulating Supply", value=circulating_supply, inline=True)
        embed.add_field(name="Last Updated (UTC)", value='%s' % last_updated[0:19], inline=True)
        embed.add_field(name="genesis", value=genesis, inline=True)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/xoxzwM3gCgR8HHCSXKh9ckQeNFDX-f8QBoruR631Udk/https/media.discordapp.net/attachments/915801233233707008/919457793600258088/i01_logo_small_icon_only_inverted_1.png")
        await ctx.send(embed=embed)
        await ctx.send(chart_thumb)


def setup(client):
    client.add_cog(Chart(client))
