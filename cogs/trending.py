# -*- coding: utf-8 -*-

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

load_dotenv()

class Trending(commands.Cog):
    """The description for Trending goes here."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="trending")
    async def trending(self, ctx):
        trending_data = cg.get_search_trending()
        # ^^Full json object recieved from API call
        trend1 = (trending_data['coins'][0]['item']['id'])
        trend2 = (trending_data['coins'][1]['item']['id'])
        trend3 = (trending_data['coins'][2]['item']['id'])
        trend4 = (trending_data['coins'][3]['item']['id'])
        trend5 = (trending_data['coins'][4]['item']['id'])
        trend6 = (trending_data['coins'][5]['item']['id'])
        # Finding the top 3 trending coins id's (btc, eth) and assigning to vars

        t1 = cg.get_price(ids=[trend1, trend2, trend3, trend4, trend5, trend6], vs_currencies=['usd'], include_24hr_change='true')
        #                       ^Getting prices of trending coins using symbols from api call above
        embed=discord.Embed(title="Invite Coinio", url="https://www.beemo.best", description="The most searched coins from the past hour and their prices.", color=0x9147ff)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/915801233233707008/919457793600258088/i01_logo_small_icon_only_inverted_1.png")
        embed.add_field(name=trend1, value="%s" % t1[trend1]['usd'], inline=True)
        embed.add_field(name=trend2, value="%s" % t1[trend2]['usd'], inline=True)
        embed.add_field(name=trend3, value="%s" % t1[trend3]['usd'], inline=True)
        embed.add_field(name=trend4, value="%s" % t1[trend4]['usd'], inline=True)
        embed.add_field(name=trend5, value="%s" % t1[trend5]['usd'], inline=True)
        embed.add_field(name=trend6, value="%s" % t1[trend6]['usd'], inline=True)
        embed.set_footer(text="Coinio, The best crypto info bot ever!")
        await ctx.send(embed=embed)


    
    

def setup(client):
    client.add_cog(Trending(client))
