from discord.ext import commands
import discord
from discord.commands import slash_command  # Importing the decorator that makes slash commands.
from discord.commands import Option
import requests
from requests.structures import CaseInsensitiveDict
import json
import pycoingecko
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import os
from dotenv import load_dotenv

class ChartSlash(commands.Cog):
    """The description for ChartSlash goes here."""

    def __init__(self, client):
        self.client = client


    @slash_command(guild_ids=[879345472815386674], description="A high quality chart with advanced indicators and expansive graph intervals")
    async def chart(self, ctx: commands.Context, *, 
                    ticker: Option(str, "Please enter the symbol of the coin", required=True),
                    interval: Option(str, "Time in", choices=["1m","3m","5m","15m","30m","45m","1h","2h","3h","4h","1d","1w"])
    ):
        coin = cg.get_coin_by_id(ticker)
        #thumb = (coin['image']['large'])
        symbol = (coin['symbol'])
        chart_thumb = ("https://api.chart-img.com/v1/tradingview/advanced-chart?symbol=%sUSD&width=800&height=400&interval=%s&theme=dark&studies=rsi" % (symbol, interval))
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
        #await ctx.respond(embed=embed)
        await ctx.respond(chart_thumb)


def setup(client):
    client.add_cog(ChartSlash(client))
