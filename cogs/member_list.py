import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone
import io

utc = timezone.utc
jst = timezone(timedelta(hours=9), "Asia/Tokyo")

class Member_list(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #サーバーメンバーのリスト取得 member_list
    @commands.command(name = 'member_list')
    async def member_list(self,ctx):
        """サーバーメンバーのリスト取得"""
        now = datetime.now(jst)
        members_list = [member for member in ctx.guild.members if member.bot == False]
        member_list = list_create(members_list)
        with io.StringIO(member_list) as list:
            await ctx.send(file = discord.File(list, filename = f"member_list<{now.strftime('%m.%d,%H.%M')}>.txt"))


def list_create(members) -> str:
    list = 'メンバー一覧\n' + 'User_Name'.ljust(20) + 'User_ID'.ljust(25) + 'Global_Name\n'
    for member in members:
            if name:= member.name:
                list += '{:<20}'.format(name) + '{:<25}'.format(member.id)
            else:
                list += '{:<20}'.format('None_name') + '{:<25}'.format(member.id)
            if global_name:= member.global_name:
                list += global_name + '\n'
            else:
                list += 'None_name\n'
    return list



def setup(bot):
    return bot.add_cog(Member_list(bot))