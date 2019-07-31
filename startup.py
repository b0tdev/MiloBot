import discord
from discord.ext import commands

class Errors(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot is Ready')
		
	@commands.Cog.listener()
	async def cog_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Please Pass All Required Arguments")
		if isinstance(error, commands.CheckFailure):
			await ctx.send("You dont have Permission to do that")
		if isinstance(error, commands.CommandNotFound):
			await ctx.send("No Command found")
		if isinstance(error, commands.ArgumentParsingError):
			await ctx.send("An Error Occured")
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Error !!!!")
		if isinstance(error, commands.BadArgument):
			await ctx.send('An Error Occured Please Retry')
			
def setup(client):
	client.add_cog(Errors(client))