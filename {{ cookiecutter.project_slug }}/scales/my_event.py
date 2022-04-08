from core.base import CustomSnake

from dis_snek import Scale, listen
from dis_snek.api.events import ChannelCreate


class CustomScale(Scale):
    bot: CustomSnake

    @listen()
    async def on_channel_create(self, event: ChannelCreate):
        """This event is called when a channel is created in a guild where the bot is"""

        self.bot.logger.info(f"Channel created with name: {event.channel.name}")


def setup(bot: CustomSnake):
    """Let dis-snek load the scale"""

    CustomScale(bot)
