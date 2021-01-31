# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('GUILD_NAME')

bot = commands.Bot(command_prefix='$')

   
@bot.command(name="Version", help="Shows bot version.")
async def on_message(message):
  
    response = os.getenv("VERSION")
    await message.channel.send(response)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run(TOKEN)
