import discord
from discord.ext import commands

class BasicCommands(commands.Cog):
	
	def __init__(self, client):
		self.cleint = client
		
	@commands.command(name="Ping", description="Shows the latency of the bot", hidden=False)
	async def ping(self, ctx):
		
		color = discord.Color.dark_gold()
		
		em = discord.Embed(title=f"Pong :ping_pong: {ctx.author.name}", description="{round(client.latency * 1000)} ms", timestap=ctx.message.created_at)
		em.set_footer(text=f"Req by {ctx.author.name}. ID: {ctx.author.id}")
		await ctx.send(embed=em)
		
	@commands.command(name="Hello", description="Greets the user", hidden=False)
	async def hello(self, ctx):
		await ctx.send(f"**Hello** {ctx.author.name}")
		
	@commands.command(name="Userinfo", description="Shows the info about the user", hidden=False)
	async def userinfo(self, ctx):
		
		color = discord.Color.dark_magenta()
		
		em = discord.Embed(title=f"User Info - {ctx.author.mention}", description=f"Show Info about {ctx.author.name}", timestap=ctx.message.created_at)
		em.add_field(name="NAME:", value=ctx.author.name)
		em.add_field(name="ID:", value=ctx.author.id)
		em.add_field(name="CREATED:", value=ctx.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		em.add_field(name="JOINED:", value=ctx.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
		await ctx.send(embed=em)
		
def setup(client):
	client.add_cog(BasicCommands(client))
	
		
		
