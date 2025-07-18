import discord
from discord.ext import commands
from conf import DISCORD_BOT_TOKEN, BOT_PREFIX
from BotEvents import setup_events
from comands import setup_Comands

def main():
    """Fungsi utama"""
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

    setup_events(bot)
    setup_Comands(bot)
    bot.run(DISCORD_BOT_TOKEN)

if __name__ == '__main__':
    main()