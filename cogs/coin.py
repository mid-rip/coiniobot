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
class Coin(commands.Cog):
    """The description for Coin goes here."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="coin")
    async def coin(self, ctx, arg1):
        coin = cg.get_coin_by_id(arg1)
        thumb = (coin['image']['large'])
        desc = (coin['description']['en'])
        symbol = (coin['symbol'])
        name = (coin['name'])
        coinsite = (coin['links']['homepage'][0])
        genesis = (coin['genesis_date'])
        usd_price = (coin['market_data']['current_price']['usd'])
        usd_price_change_24h = (coin['market_data']['price_change_24h'])       
        total_supply = (coin['market_data']['total_supply'])  
        circulating_supply = (coin['market_data']['circulating_supply'])
        last_updated = (coin['market_data']['last_updated'])
        twit_follows = (coin['community_data']['twitter_followers'])  
        reddit_subs = (coin['community_data']['reddit_subscribers'])  
        usd_price_change_percent_24h = (coin['market_data']['price_change_percentage_24h'])  
        trust_score = (coin['tickers'][0]['trust_score'])


        embed=discord.Embed(title=name, url=coinsite, description="Genesis block: %s " % genesis, color=0x8652ff)
        embed.set_author(name="Coinio", url="https://www.beemo.best", icon_url="https://images-ext-2.discordapp.net/external/xoxzwM3gCgR8HHCSXKh9ckQeNFDX-f8QBoruR631Udk/https/media.discordapp.net/attachments/915801233233707008/919457793600258088/i01_logo_small_icon_only_inverted_1.png")
        embed.add_field(name="Description", value=desc[0:600], inline=False)
        embed.add_field(name="Price per coin", value='$%s USD' % usd_price, inline=True)
        embed.add_field(name="Price Change (24h)", value='$%s USD' % usd_price_change_24h, inline=True)
        embed.add_field(name="Price Change % (24h)", value='%s' % usd_price_change_percent_24h, inline=True)
        embed.add_field(name="Total Supply", value='%s' % total_supply, inline=True)
        embed.add_field(name="Circulating Supply", value='%s' % circulating_supply, inline=True)
        embed.add_field(name="Last Updated (UTC)", value='%s' % last_updated[0:19], inline=True)
        embed.add_field(name="Twitter Follows", value='%s' % twit_follows, inline=True)
        embed.add_field(name="Reddit Subscribers", value='%s' % reddit_subs, inline=True)
        embed.add_field(name="Trust Score", value='%s' % trust_score, inline=True)
        embed.set_footer(text="Coinio, The best crypto info bot ever!")
        embed.set_thumbnail(url=thumb)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Coin(client))
