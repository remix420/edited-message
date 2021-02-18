import discord
from discord.ext import tasks
import asyncio

token = ''


client = discord.Client()


@client.event
async def on_message(message):
	if message.author == client.user:
		await message.edit(content=message.content)
		
		
client.run(token, bot=False)
