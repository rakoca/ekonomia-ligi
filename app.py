import discord
from discord.ext import commands
from variables import PREFIX, DESC
import asyncio
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix=PREFIX,
    description=DESC,
    intents=intents
)
async def load():
   for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
   await load()
   token = open('token')
   await bot.start(token.read())
   token.close()

asyncio.run(main())