import discord
from discord.ext import commands

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
async def addmem(ctx, name: discord.Member, lang="Python"):
	try:
		with open("data.json", "r") as f:
			file = json.load(f)

		with open("names.json", "r") as f:
			data = json.load(f)	

		if name not in file:	

			file[str(name.id)] = lang
			data[str(name.id)] = name

			with open("data.json", "w") as f:
				json.dump(file, f)
			with open("names.json", "w") as f:
				json.dump(data, f)	

			await ctx.send('User has been successfuly added.')	

		elif name in file:
			await ctx.send('User is already in database.')
		else:
			raise Exception("smth")
	except Exception as e:
		await ctx.send(e)

@client.command()
async def removemem(ctx, name):
		with open("data.json", "r") as f:
			file = json.load(f)

		if name in file:
			del file[str(name)]
			await ctx.send('User has been successfuly removed.')
		elif name not in file:
			await ctx.send("User not found.")
		else:
			raise Exception("smth else")

@client.command()
async def viewmem(ctx):
		with open("names.json", "r") as f:
			file = json.load(f)
		mem = ""
		c = 0
		
		for i in file:
			c += 1
			mem.join(f"[{c}] {i}\n")

	
#Run		

client.run('Nzk1NTA4ODUwMDM5ODQ4OTgw.X_KZWQ.KvEAP-Qe0BqV8rux5qAJd2FFPoM')	