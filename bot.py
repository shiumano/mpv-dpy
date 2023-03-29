import discord
from discord.ext import commands
import glob
from config import TOKEN

bot = commands.Bot(command_prefix='y%')

@bot.event
async def on_ready():
    print('Bot ready')
    for file in glob.glob("cogs/*.py"):
        await bot.load_extension(file.replace('/', '.')[:-3])

bot.run(TOKEN)