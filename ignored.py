import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="m-")

@client.command(name="load", discription="Loads a cog", hidden=True)
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	await ctx.send('Successfully loaded')
	
@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	await ctx.send('Successfully unloaded')
	
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f"cogs.{filename[:-3]}")
		
client.run(os.getenv("TOKEN"))