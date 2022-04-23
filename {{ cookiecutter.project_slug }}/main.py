import os

from dis_snek.ext.debug_scale import DebugScale
from dotenv import load_dotenv

from core.logging import init_logging
from core.base import CustomSnake
from core.scales_loader import load_scales

from dis_snek import Intents


if __name__ == "__main__":
    # load the environmental vars from the .env file
    load_dotenv()

    # initialise logging
    init_logging()

    # create our bot instance
    bot = CustomSnake(
        intents=Intents.DEFAULT,  # intents are what events we want to receive from discord, `DEFAULT` is usually fine
        auto_defer=True,  # automatically deferring interactions
        activity="A dis-snek bot",  # the status message of the bot
    )

    # load the debug scale if that is wanted
    if (dev_guild_id := os.getenv("LOAD_DEBUG_COMMANDS")) == "true":
        debug_scale = DebugScale(bot=bot)

    # load all scales in the ./scales folder
    load_scales(bot=bot)

    # start the bot
    bot.start(os.getenv("DISCORD_TOKEN"))
