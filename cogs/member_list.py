import discord
from discord.ext import commands

class Member_list(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #サーバーメンバーのリスト取得 member_list
    @commands.command(name = 'member_list')
    async def member_list(self,ctx):
        """サーバーメンバーのリスト取得"""
        members_list = [member for member in ctx.guild.members if member.bot == False]
        member_list = 'メンバー一覧\n'
        for member in members_list:
            if member.bot == True:
                continue
            if member_name:= member.global_name:
                member_list += str(member_name + '\n')
                print(member_name)
            else:
                member_list += str(member.name + '\n')
                print(member.name)
        await ctx.send(content = member_list)

def setup(bot):
    return bot.add_cog(Member_list(bot))