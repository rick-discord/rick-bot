import discord
import os
import json
import time
from discord.ext import commands, tasks
from random import choice
from replit import db

client = commands.Bot(command_prefix=('-', 'rick '), intents=discord.Intents.default())

@client.command(name='load')
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')


@client.command(name='unload')
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    change_status.start()
    print('BUuuUrp, whhooo im online baby')



#----------status----------
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


status = [
    '-help', 'made by doof.exe#8028 and Trevi4kо#2636', 'BuUuURp',
    'wabalabadubdub', 'and thats the way the news gos'
]

client.run(os.getenv('TOKEN'))
