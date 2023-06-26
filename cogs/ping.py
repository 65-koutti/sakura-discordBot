import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #生存確認用コマンド ping
    @commands.command(name = "ping")
    async def ping(self, ctx):
        """生存確認用コマンド"""
        await ctx.reply(content = 'pong')
        return

def setup(bot):
    return bot.add_cog(Ping(bot))