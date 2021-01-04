import discord
import os
from discord.ext import commands
from subprocess import run

with open('token.txt', 'r') as f:
	TOKEN = str(f.readline())

client = commands.Bot(command_prefix = 'py ')

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
async def lineit(ctx, *, args):
	with open("tester.py", "r") as f:
		file = f.readlines()

	c = 0
	txt = ""

	for line in file:
		c += 1
		txt += "```py\n" + str(c) + " " + line + "```"
	await ctx.send(f'{txt}')

@client.command()
async def errs(ctx, *, args):
	with open("tester.py", "w") as f:
		f.write(args)
	try:
		os.system('python tester.py')

	except Exception as e:		
		await ctx.send(f"WARNING:\n{e}")

	
#Run		

client.run(TOKEN)	