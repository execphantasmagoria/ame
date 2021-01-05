import discord
import os
from discord.ext import commands
import sys
import asyncio

with open('token.txt', 'r') as f:
	TOKEN = str(f.readline())

client = commands.Bot(command_prefix = 'py ')

#Events

@client.event
async def on_ready():
	print("bot is ready")
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('[py] Reading doujins'))

#Helpers

def rump(source_code):

	with open("tester.py", "w") as f:
		f.write(f'import sys\n\nsys.stdout = open("out.txt", "w")\n\n{source_code}\n\nsys.stdout.close()')

	with open("tester.py", "r") as f:
		code = compile(f.read(), "tester.py", "exec")
	exec(code)

	with open("out.txt", "r") as output:
		msg = output.readline()
	return msg


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

@client.command()
async def run(ctx, *, args):

	with open("tester.py", "w") as f:
		f.write(f'import sys\n\nsys.stdout = open("out.txt", "w")\n\n{args}\n\nsys.stdout.close()')

	with open("tester.py", "r") as f:
		code = compile(f.read(), "tester.py", "exec")
	exec(code)

	with open("out.txt", "r") as output:
		msg = output.readline()
		await ctx.send(msg)

@client.command()
async def shell(ctx):
	await ctx.send('Are you sure you want to activate shell? (y/n)')

	msg = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
	
	if msg.content == "y":
		message = await ctx.send('Booting shell in... 3')
		await asyncio.sleep(1)
		await message.edit(content="Booting shell in... 2")
		await asyncio.sleep(1)
		await message.edit(content="Booting shell in... 1")
		await asyncio.sleep(1)
		await message.edit(content="Booted up!")
		await asyncio.sleep(1)
		await message.edit(content=f"**__PYTHON SHELL ACTIVE__** *via* {ctx.author.mention}//")

		source = ""
		shell_res_cmd = ["code", "run", "terminate", "clr", "lclr"]

		while True:
			cmd = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel.id)
			
			if cmd.content not in shell_res_cmd:
				last = cmd.content
				source += cmd.content.replace(",,", "    ") + "\n"
			elif cmd.content == "code":
				if source == "":
					await ctx.send('Nothing here.')
				else:
					await ctx.send(f'```py\n{source}```')
			elif cmd.content == "run":
				try:
					shell_out = rump(source)
					await ctx.send(shell_out)
				except Exception as e:
					await ctx.send(f':red_square: __WARNING__ :red_square: :\n{e}\nUse `py check` on the code for  details.')	
			elif cmd.content == "clr":
				source = ""
				await ctx.send('Shell cleared.')
			elif cmd.content == "lclr":
				if last != None:
					source = source.replace(last, "")
					await ctx.send('Last input cleared.')
				else:
					await ctx.send('Cannot clear inputs older than last. Use `clr` to clear shell.')	
					
			elif cmd.content == "terminate":
				close_msg = await ctx.send('Terminating shell...')
				await asyncio.sleep(2)
				await close_msg.edit(content="Shell terminated.")
				break
			else:
				await ctx.send('Error')
				break

	else:
		await ctx.send('Process aborted.')		
	
#Run		

client.run(TOKEN)	
