import logging
import os

from dis_snek import Snake, listen


class CustomSnake(Snake):
    """Subclass of dis_snek.Snake with our own logger and on_startup event"""

    # you can use that logger in all your scales
    logger = logging.getLogger(os.getenv("LOGGER_NAME"))

    @listen()
    async def on_startup(self):
        """Gets triggered on startup"""

        self.logger.info(f"{os.getenv('PROJECT_NAME')} - Startup Finished!\n")
        self.logger.info(
            "Note: Discord needs up to an hour to load your commands / context menus. They may not appear immediately"
        )
