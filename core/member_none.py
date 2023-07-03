import discord
from discord.ext import commands

class Member_none(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #memberロール未取得者にDM送信
    @commands.command(name = 'member_none')
    async def member_none(self,ctx):
        """memberロール未取得者にDM送信"""
        members_list = [member for member in ctx.guild.members if member.bot == False]
        none_roles = 'DM送信者一覧\n'
        for member in members_list:
            if member.get_role(1097832443031080983) == None :   #メンバーロールを判定
                none_roles += str(member.name + '\n')
                user = self.bot.get_user(member.id)
                text = 'これはテストです。'
                await user.send(content = text)
        await ctx.send(content = none_roles)


async def setup(bot):
    await bot.add_cog(Member_none(bot))