import discord
from discord.ext import commands
import config
from core.embed_creater import EmbedCreater as EC

GUILD_ID = str(config.GUILD_ID)
JL_LOG_CHANNEL = int(config.JOIN_LEFT_LOG_CHANNEL)

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener(name = 'on_member_join')
    async def Join_log(self, member: discord.member):
        guild = self.guild
        chanenl = guild.get_channel(JL_LOG_CHANNEL)
        embed = EC().jo_le_log(member, 'Join')
        await chanenl.send(embed = embed)





async def setup(bot):
    await bot.add_cog(
        Logging(bot),
        guilds = [discord.Object(GUILD_ID)]
    )