import discord
import os
import discord
import time
from discord.ext import commands, tasks
from discord.ext.commands import Cog
from random import choice

client = commands.Bot(command_prefix=('-', 'rick '),
                      intents=discord.Intents.default())


class fun(Cog):
    def __init__(self, client):
        self.client = client


@Cog.listener()
async def on_ready(self):
    print('fun online')


@commands.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')


@commands.command(name='prefix', help='states the prefix of the server')
async def prefix(ctx):
    await ctx.send(
        'the prefix is eather - or rick (custom per server prefixes coming soon)'
    )


@commands.command(name='servers', help='tells how many servers the bot is in')
async def servers(ctx):
    await ctx.send("BUuuUrp I'm in " + str(len(client.guilds)) + " servers!")


@commands.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `doof.exe#8028` and `Trevi4kо#2636`')


@commands.command(name='invite', help='This command returns the invite url')
async def invite(ctx):
    await ctx.send(
        'https://discord.com/api/oauth2/authorize?client_id=887063707568463872&permissions=8&scope=bot'
    )


@commands.command(name='welcome', aliases=[], help='sends a welocme gif')
async def welcome(ctx):
    responses = [
        'https://tenor.com/bwdQC.gif', 'https://tenor.com/bwwU4.gif',
        'https://tenor.com/bjDmu.gif', 'https://tenor.com/bf29v.gif'
    ]
    await ctx.send(choice(responses))


def setup(client):
    client.add_cog(fun(client))
