import discord
import os
import discord
import time
from discord.ext import commands, tasks
from random import choice

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.Cog.listener()
async def on_ready(self):
  print('online')


@commands.command(name='hello', help='This command returns a random welcome message')
async def hello(self, ctx):
    responses = [
        'what the fuck do you want now', 'wabalabadubdub im rick fuck ya',
        'what, im fucking jesus BITTTCH', 'wabalabadubdub',
        'BUuUUrp, sup bitch'
    ]
    await ctx.send(choice(responses))


@commands.command(name='penis',
                aliases=['pp', 'dick'],
                help='This command makes a pp')
async def penis(self, ctx):
    await ctx.send('╰U╯')


@commands.command(name='balls',
                aliases=['ball', 'nut', 'sack', 'nuts'],
                help='This command makes BALLLS')
async def balls(self, ctx):
    await ctx.send('oo')


@commands.command(name='gay', aliases=['sus'], help='post GAAAAY gif')
async def gay(self, ctx):
    await ctx.send(
        'https://tenor.com/view/rick-and-morty-gay-insult-gif-12293667')


@commands.command(name='4k', help='post a gif when someone is caught in 4k')
async def fourk(self, ctx):
    responses = [
        'https://c.tenor.com/QA6mPKs100UAAAAC/caught-in.gif',
        'https://i.kym-cdn.com/photos/images/facebook/002/001/991/72f',
        'https://www.meme-arsenal.com/memes/a7dd88c29f3d26bb850969619104acbd.jpg',
        'https://imgur.com/lZMSNgM', 'https://imgur.com/CjjlSDH',
        'https://imgur.com/UVv6SAW', 'https://imgur.com/tf0VGek'
    ]
    await ctx.send(choice(responses))


@commands.command(name='gif', help='This command returns a random rick gif')
async def gif(self, ctx):
    responses = [
        'https://tenor.com/view/rick-and-morthy-dance-rick-sanchez-gif-15008172',
        'https://tenor.com/view/rick-and-morty-wubbalubbadubdub-gif-8257661',
        'https://tenor.com/view/dance-morty-rick-and-morty-moves-shake-hips-gif-14488137',
        'https://tenor.com/view/dance-morty-rick-and-morty-moves-shake-hips-gif-14488137',
        'https://tenor.com/view/rick-fortnite-rick-fortnite-rick-and-morty-rick-and-morty-fortnite-gif-21873524',
        'https://tenor.com/view/rick-and-morty-rick-and-morty-season3-adult-swim-rick-sanchez-pickle-rick-gif-9088343'
    ]
    await ctx.send(choice(responses))


@commands.command(name='poop',
                aliases=['shit', 'doodoo'],
                help='post shit emoji')
async def poop(self, ctx):
    await ctx.send('༼ ºل͟º ༽')


@commands.command(name='18+', aliases=['18'])
async def chill(self, ctx):
    await ctx.send('YO WHAT U DOIN LOOKIN AT 18+ MAN')


@commands.command(name='dm')
async def dm(self, ctx):
    await ctx.author.send('slidin in the dms')


@commands.command(name='nuke', help='nukes the server')
async def nuke(self, ctx):
    await ctx.send('**NUKING SERVER**')
    time.sleep(1)
    await ctx.send('**deleting all channels**')
    time.sleep(2)
    await ctx.send('**deleting all roles**')
    time.sleep(2)
    await ctx.send('**removing owner from server**')
    time.sleep(2)
    await ctx.send('**DONE**')


@commands.command(name='cap', help='send a cap msg')
async def cap(self, ctx):
    responses = [
        'https://tenor.com/view/cap-stop-the-lying-gif-18330929',
        'https://tenor.com/view/thats-cap-youre-lying-false-wrong-fake-news-gif-13870788',
        ':billed_cap:'
    ]
    await ctx.send(choice(responses))


def setup(client):
  client.add_cog(fun(client))