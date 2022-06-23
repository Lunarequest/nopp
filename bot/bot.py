import hikari, lightbulb, os
from lightbulb import BotApp


def create_bot(token: str) -> BotApp:
    bot = lightbulb.BotApp(
        token=token,
        prefix="!",
        intents=hikari.Intents.ALL,
    )

    os.chdir("bot")
    bot.load_extensions_from("./extensions", must_exist=True)
    return bot
