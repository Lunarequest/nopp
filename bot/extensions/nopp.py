import os
import hikari
import lightbulb


nopp: lightbulb.Plugin = lightbulb.Plugin("nopp")


@nopp.listener(hikari.MessageCreateEvent)
async def on_message(event: hikari.MessageCreateEvent):
    if event.is_human:
        message = event.message.content.lower().split(" ")
        pp_list = [i for i in message if i.startswith("p")]
        if len(pp_list) != len(set(pp_list)):
            await event.message.delete()


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(nopp)
