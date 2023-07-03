import discord
from discord.ext import commands
from discord import app_commands
import config

GUILD_ID = config.GUILD_ID

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Cog再読み込みコマンド

    @app_commands.command(name = "reload", description = 'Cog再読み込みコマンド')
    async def reload(self, interaction: discord.Interaction, module_name: str):
        await interaction.response.send_message(f" モジュール[{module_name}]の再読み込みを開始します。")
        try:
            await self.bot.reload_extension(module_name)
            await interaction.followup.send(f" モジュール[{module_name}]の再読み込みを終了しました。")
        except (commands.errors.ExtensionNotLoaded, commands.errors.ExtensionNotFound,
                commands.errors.NoEntryPointError, commands.errors.ExtensionFailed) as e:
            await interaction.followup.send(f" モジュール[{module_name}]の再読み込みに失敗しました。理由：{e}")


async def setup(bot):
    await bot.add_cog(
        Reload(bot),
        guilds = [discord.Object(GUILD_ID)]
        )