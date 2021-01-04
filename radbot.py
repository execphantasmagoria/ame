import discord
import os
from discord.ext import commands
import json

#global var

#Setup

client = commands.Bot(command_prefix = get_prefix)

#Events

@client.event
async def on_ready():
	print("bot is ready")
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('[ame] Failing at reCAPTCHA.'))	


#-----------------------------------------------------------------------------------------------------------------

client.remove_command('help')

#Checks
	

#Cogs



#Commands		



#Helpers


#Run		

client.run('')	