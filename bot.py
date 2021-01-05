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
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('[py] Reading doujins'))	

#Commands		

@client.command()
async def kilu(ctx):
	await ctx.send('Killerok, do your assignment.')

@client.command()
async def lineit(ctx, *, args):
	with open("tester.py", "w") as f:
		f.write(args)

	with open("tester.py", "r") as f:
		file = f.readlines()

	c = 0
	txt = ""

	for line in file:
		c += 1
		txt += "```py\n" + str(c) + "   " + line + "```"

	await ctx.send(txt)

@client.command()
async def check(ctx, *, args):
	with open("tester.py", "w") as f:
		f.write(args)

	try:
		with open("tester.py", "r") as f:
			code = compile(f.read(), "tester.py", "exec")
		exec(code, globals, locals)
		await ctx.send('No errors. Code is clean.')
	except Exception as e:
		foo = str(e)
		li = foo.split()
		for i in li:
			if i == "line":
				inx = li.index(i)
				ern = li[inx+1]
				ern = ern.replace(")", "")

		with open("tester.py", "r") as f:
			file = f.readlines()

		c = 0
		txt = ""

		for line in file:
			c += 1
			if int(c) == int(ern):
				txt += "```py\n" + "‣" + str(c) + "   " + line + "```"
			else:	
				txt += "```py\n" + str(c) + "   " + line + "```"

		await ctx.send(txt)
		await ctx.send(f':red_square: __WARNING__ :red_square: :\n{e}')





	
#Run		

client.run(TOKEN)	