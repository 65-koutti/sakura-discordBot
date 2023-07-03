import discord
from datetime import datetime, timedelta, timezone

utc = timezone.utc
jst = timezone(timedelta(hours=9), "Asia/Tokyo")

class EmbedCreater:
    def __init__(self) -> None:
        pass

    def jo_le_log(member: discord.member, status: str) -> discord.Embed:
        now = datetime.now(jst)
        if status == 'Join':
            embed = discord.Embed(
            title = f'Member {status}d',description = f'{member.mention}がサーバーに参加しました。',color = discord.Colour.green())
            embed.add_field(name = 'アカウント作成日', value = f'{member.created_at.strftime("%m/%d %H:%M:%S")}')
            embed.add_field(name = 'その他情報', value = f'現在のサーバー人数:{member.guild.member_count}\n')
        elif status == 'Left':
            embed = discord.Embed(
            title = f'Member {status}',description = f'{member.mention}がサーバーから退出しました。',color = discord.Colour.yellow())
            embed.add_field(name = 'サーバー参加日', value = f'{member.joined_at.strftime("%m/%d %H:%M:%S")}')
        if global_name:= member.global_name:
            name = global_name
        else:
            name = member.name
        embed.set_author(name = name, icon_url = member.guild_avatar.url)
        embed.set_footer(text = f'{member.id}・{now.strftime("%m/%d %H:%M:%S")}')
        return embed