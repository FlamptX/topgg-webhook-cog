from discord.ext import commands
from configparser import ConfigParser
parser = ConfigParser()
parser.read("config.txt")
TOKEN = parser.get('config', 'token')

bot = commands.Bot(command_prefix='!')

bot.load_extension("Webhook")

bot.run(TOKEN)
