import discord
import os
import json
from discord.ext import commands, tasks
from discord_buttons_plugin import  *
from random import choice
from replit import db


client = commands.Bot (command_prefix=('-', 'rick '))
buttons = ButtonsClient(client)
db["test"] = ""

@client.event
async def on_ready():
    change_status.start()
    print('BUuuUrp, whhooo im online baby')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')
    
@client.command(name='prefix', help='states the prefix of the server')
async def prefix(ctx):
    await ctx.send('the prefix is eather - or rick (custom per server prefixes coming soon)')

@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['what the fuck do you want now', 'wabalabadubdub im rick fuck ya', 'what, im fucking jesus BITTTCH', 'wabalabadubdub', 'BUuUUrp, sup bitch']
    await ctx.send(choice(responses))

@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by `doof.exe#8028` and `Trevi4kо#2636`')

@client.command(name='invite', help='This command returns the invite url')
async def invite(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=887063707568463872&permissions=8&scope=bot')

@client.command(name='penis', aliases=['pp', 'dick'] , help='This command makes a pp')
async def penis(ctx):
    await ctx.send('╰U╯')

@client.command(name='gay', aliases=['sus'], help='post GAAAAY gif')
async def gay(ctx):
    await ctx.send('https://tenor.com/view/rick-and-morty-gay-insult-gif-12293667')

@client.command(name='4k', help='post a gif when someone is caught in 4k')
async def caughtin4k(ctx):
  responses = ['https://c.tenor.com/QA6mPKs100UAAAAC/caught-in.gif', 'https://i.kym-cdn.com/photos/images/facebook/002/001/991/72f', 'https://www.meme-arsenal.com/memes/a7dd88c29f3d26bb850969619104acbd.jpg', 'https://imgur.com/lZMSNgM', 'https://imgur.com/CjjlSDH', 'https://imgur.com/UVv6SAW', 'https://imgur.com/tf0VGek']
  await ctx.send(choice(responses))

@client.command(name='gif', help='This command returns a random rick gif')
async def gif(ctx):
    responses = ['https://tenor.com/view/rick-and-morthy-dance-rick-sanchez-gif-15008172', 'https://tenor.com/view/rick-and-morty-wubbalubbadubdub-gif-8257661', 'https://tenor.com/view/dance-morty-rick-and-morty-moves-shake-hips-gif-14488137', 'https://tenor.com/view/dance-morty-rick-and-morty-moves-shake-hips-gif-14488137', 'https://tenor.com/view/rick-fortnite-rick-fortnite-rick-and-morty-rick-and-morty-fortnite-gif-21873524', 'https://tenor.com/view/rick-and-morty-rick-and-morty-season3-adult-swim-rick-sanchez-pickle-rick-gif-9088343']
    await ctx.send(choice(responses))

@client.command(name='roll', aliases=['dice', 'diceroll'], help='This command rolls a dice')
async def roll(ctx):
    responses = ['1', '2', '3', '4','5', '6']
    await ctx.send(choice(responses))

@client.command(name='poop', aliases=['shit', 'doodoo'] , help='post shit emoji')
async def credits(ctx):
    await ctx.send('༼ ºل͟º ༽')

#status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
status = ['-help', 'made by doof.exe#8028', 'BuUuURp', 'wabalabadubdub', 'and thats the way the news gos']

client.run(os.getenv('TOKEN'))