import discord
from discord.ext import commands

class Moderation(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def kick(self, ctx, member : discord.Member = None, reason = None):
		if member == None:
			await ctx.send(f"Please Select A Member to kick {ctx.author.mention}")
		if member == ctx.message.author:
			await ctx.send(f"You Cannot Kick Yourself {ctx.author.mention}")
		if reason == None:
			reason = f"Please Specify a reason to kick {ctx.author.mention}"
		message = f"You Have Been kicked Out from **{ctx.guild.name}** for **{reason}**, Kicked by : {ctx.author.name}"
		await member.send(message)
		await ctx.guild.kick(member)
		await ctx.channel.send(f"Hello, A kick has been happend for {member} by {ctx.author.name} !!")
			