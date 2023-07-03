import discord
from discord.ext import commands

class Member_none_list(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #memberロール未取得者のリスト取得 member_none_list
    @commands.command(name = 'member_none_list')
    async def member_none_list(self,ctx):
        """memberロール未取得者のリスト取得"""
        none_roles = 'Memberロール未取得者一覧\n'
        members_list = [member for member in ctx.guild.members if member.bot == False]
        for member in members_list:
            if member.get_role(1097832443031080983) == None :
                none_roles += str(member.name + '\n')
        await ctx.send(content = none_roles)
async def setup(bot):
    await bot.add_cog(Member_none_list(bot))