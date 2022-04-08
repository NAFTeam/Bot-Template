import logging
import os

from dis_snek import Snake, listen, logger_name


class CustomSnake(Snake):
    """Subclass of dis_snek.Snake with our own logger and on_startup event"""

    # you can use that logger in all your scales
    logger = logging.getLogger(logger_name)

    @listen()
    async def on_startup(self):
        """Gets triggered on startup"""

        self.logger.info(f"{os.getenv('PROJECT_NAME')} - Startup Finished!")
        self.logger.info(
            "Note: Discord needs up to an hour to load your commands / context menus. They may not appear immediately\n"
        )
