import discord
from discord.ext import commands
import random
import os
import json

client = commands.Bot(command_prefix="m-")

@client.event
async def on_ready():
	print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nVersion: {discord.__version__}\nAuthor: {discord.__author__}\nCopyrights: {discord.__copyright__}\nBuild Class: {discord.__package__}')
	
client.run(os.getenv("TOKEN"))
