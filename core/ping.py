import discord
from discord.ext import commands
from discord import app_commands
import config

GUILD_ID = config.GUILD_ID

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #生存確認用コマンド ping
    @app_commands.command(name = "ping",description = '生存確認用コマンド')
    async def ping(self, interaction: discord.Interaction):
        # interactionは3秒以内にレスポンスしないといけないとエラーになるのでこの処理を入れる。
        await interaction.response.defer()
        latency: float = self.bot.latency
        latency_ms: int = round(latency * 1000)
        await interaction.followup.send(f'Pong! ({latency_ms}ms)')
        return

async def setup(bot):
    await bot.add_cog(
        Ping(bot),
        guilds = [discord.Object(GUILD_ID)]
    )