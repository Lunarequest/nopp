from bot import create_bot
import os

bot = create_bot(os.environ["BOT_TOKEN"])

# if os.name != "nt":
#    import uvloop
#
#    uvloop.install()

bot.run()
