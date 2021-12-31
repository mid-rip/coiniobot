from discord.commands import slash_command  # Importing the decorator that makes slash commands.
from discord.ext import commands
import requests
from requests.structures import CaseInsensitiveDict
import json
import pycoingecko
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import os
from dotenv import load_dotenv
import discord

defi_data = cg.get_global_decentralized_finance_defi()





class Defi(commands.Cog):
    """The description for Defi goes here."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="defi")
    async def defi(self, ctx):
        defi_data = cg.get_global_decentralized_finance_defi()
        defiethratio = defi_data['defi_to_eth_ratio']
        defi_cap = defi_data['defi_market_cap']
        eth_cap = defi_data['eth_market_cap']
        top_coin = defi_data['top_coin_name']
        top_coin_dom = defi_data['top_coin_defi_dominance']

        embed=discord.Embed(title="DeFi Information", url="https://www.beemo.best", description="Everything you need to know about DeFi", color=ctx.author.color)
        embed.add_field(name="DeFi/ETH Ratio", value=defiethratio[0:15], inline=True)
        embed.add_field(name="DeFi Market Cap", value='$%s USD' % defi_cap[0:14], inline=True)
        embed.add_field(name="ETH Market Cap", value='$%s USD' % eth_cap[0:14], inline=True)
        embed.add_field(name="Top DeFi Coin", value=top_coin, inline=True)
        embed.add_field(name="Top DeFi Coin Dominance", value ='%s' % top_coin_dom, inline=True)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/xoxzwM3gCgR8HHCSXKh9ckQeNFDX-f8QBoruR631Udk/https/media.discordapp.net/attachments/915801233233707008/919457793600258088/i01_logo_small_icon_only_inverted_1.png")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Defi(client))
