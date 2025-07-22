from discord.ext import commands
import discord
from scraper import scrape_news
from conf import   NEWS_URL, USE_BURP_PROXY, BURP_PROXY_HOST, BURP_PROXY_PORT

def setup_Comands(bot):
    """
    Function to setup events when bot starts
    """

    @bot.command(name='hello')
    async def hello(ctx):
        """send message"""
        await ctx.send('Hello!')

    @bot.command(name='goodbye')
    async def goodbye(ctx):
        """send message"""
        await ctx.send('Goodbye!')

    @bot.command(name='berita')
    async def berita(ctx):
        """Take a newspapper"""

        await ctx.send("Take a rest when i took the newspapper")
        news = await scrape_news(
            NEWS_URL,
            USE_BURP_PROXY,
            BURP_PROXY_HOST,
            BURP_PROXY_PORT
        )

        if news:
            message = "**BERITA:**\n"
            for item in news:
                message += f"• **{item['title']}**\n"
                message += f"  <{item['link']}>\n"
            await ctx.send(message)
        else:
            await ctx.send("Maaf, tidak dapat mengambil berita terkini saat ini. Mungkin ada masalah dengan situs web atau koneksi.")
