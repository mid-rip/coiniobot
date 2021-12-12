# -*- coding: utf-8 -*-

from discord.ext import commands
import discord

class Mycog(commands.Cog):
    """The description for Mycog goes here."""

    def __init__(self, client):
        self.client = client

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("uwu")

def setup(client):
    client.add_cog(Mycog(client))
