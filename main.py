import discord
from discord.ext import commands
from datetime import datetime, timedelta, timezone
import logging
import traceback
import config


#ログの宣言、フォーマットの指定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
    filename="discord.log"
    )


#utc, jstの取得(世界標準時、日本標準時)
utc = timezone.utc
jst = timezone(timedelta(hours=9), "Asia/Tokyo")

#HelpCommandの指定
class JapaniseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = 'コマンド:'
        self.no_category = 'その他'
        self.command_attrs['help'] = 'コマンド一覧と簡単な説明を表示'

    def get_ending_note(self) -> str:
        return (f'各コマンドの説明: //help <コマンド名>\n')

#discordBOTのIntentを取得
intents = discord.Intents.all()
intents.typing = False

#コグの一覧を明記
INITIAL_EXTENSIONS = [
    'cogs.ping',
    'cogs.member_none_list',
    'cogs.member_list',
    'cogs.member_none'
    ]


# コグとして用いるクラスを定義。
class MyBot(commands.Bot):
    def __init__(self):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(
            command_prefix='//',
            intents=intents,
            status = discord.Status.online,
            activity = discord.Activity(
                type = discord.ActivityType.listening,
                name = "てぇてぇを監視中"
            ),
            help_command=JapaniseHelpCommand()
        )

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()
            else:
                print(f'extension [{cog}] is loaded!')


    #Bot起動時の動作
    async def on_ready(self):
        channel = self.get_channel(1122132290454179931)
        now = datetime.now(jst)
        for cog in INITIAL_EXTENSIONS:
            try:
                self.reload_extension(cog)
            except Exception:
                traceback.print_exc()
            else:
                print(f'extension [{cog}] is reloaded!')
        await channel.send(
            f"起動完了({now.strftime('%m/%d %H:%M:%S')})\nBot ID:{self.user.id})"
        )
        print('-------------------------------------')
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")
        print('-------------------------------------')
        return

bot = MyBot()

TOKEN = config.TOKEN

if __name__ == '__main__':
    bot.run(token = TOKEN)