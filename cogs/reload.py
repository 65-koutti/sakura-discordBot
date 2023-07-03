import discord
from discord.ext import commands

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Cog再読み込みコマンド

    @commands.is_owner()
    @commands.command(name = "reload")
    async def reload(self, ctx, module_name):
        """Cog再読み込みコマンド"""
        await ctx.send(f" モジュール[{module_name}]の再読み込みを開始します。")
        try:
            await self.bot.reload_extension(module_name)
            await ctx.send(f" モジュール[{module_name}]の再読み込みを終了しました。")
        except (commands.errors.ExtensionNotLoaded, commands.errors.ExtensionNotFound,
                commands.errors.NoEntryPointError, commands.errors.ExtensionFailed) as e:
            await ctx.send(f" モジュール[{module_name}]の再読み込みに失敗しました。理由：{e}")
            return

def setup(bot):
    return bot.add_cog(Reload(bot))