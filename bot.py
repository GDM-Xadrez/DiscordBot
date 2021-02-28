# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from cogwatch import Watcher

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
GUILD = os.getenv('GUILD_NAME')
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    watcher = Watcher(bot, path='cogs', debug=False)
    await watcher.start()

extensions = [
    "cogs.Aberturas",
    "cogs.Puzzles",
    "cogs.BotInfo"
    ]

if __name__ == "__main__":
    for ext in extensions:
        bot.load_extension(ext)

bot.run(TOKEN)
