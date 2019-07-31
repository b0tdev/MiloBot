import discord
from discord.ext import commands

import random
import json

class Fun(commands.Cog):
	
	def __init__(self, client):
		self.client = client
		
	@commands.command()
        async def randomcomic(self, ctx):
        '''Get a comic from xkcd.'''
          async with aiohttp.ClientSession() as session:
            async with session.get(f'http://xkcd.com/info.0.json') as resp:
              data = await resp.json()
              currentcomic = data['num']
          rand = random.randint(0, currentcomic)  # max = current comic
          async with aiohttp.ClientSession() as session:
            async with session.get(f'http://xkcd.com/{rand}/info.0.json') as resp:
              data = await resp.json()
          em = discord.Embed(color=discord.Color.green())
          em.title = f"XKCD Number {data['num']}- \"{data['title']}\""
          em.set_footer(text=f"Published on {data['month']}/{data['day']}/{data['year']}")
          em.set_image(url=data['img'])
          await ctx.send(embed=em)

def setup(client):
	client.add_cog(Fun(client))
