import discord
import os
from discord.ext import commands
from subprocess import run

with open('token.txt', 'r') as f:
	TOKEN = str(f.readline())

client = commands.Bot(command_prefix = 'a.')

#Events

@client.event
async def on_ready():
	print("bot is ready")
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('[a.] Failing at reCAPTCHA.'))	

#Commands		

@client.command()
async def kilu(ctx):
	await ctx.send('Killerok, do your assignment.')

@client.command()
async def code(ctx, *, args):
	await ctx.send(args)

@client.command()
async def run(ctx, *, args):
	with open("tester.py", "w") as f:
		f.write(args)
	try:
		os.system('python tester.py')

	except Exception as e:		
		await ctx.send(f"WARNING:\n{e}")

	
#Run		

client.run(TOKEN)	