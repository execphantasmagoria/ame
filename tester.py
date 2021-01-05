import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

#Events

@client.event
async def on_ready():
    print("bot is ready")

#Commands

@client.command()
async def smth(ctx):
    ctx.send('hello!')

@client.command()
async def again(ctx, msg):
    ctx.send(msg

#Run        

client.run('---')