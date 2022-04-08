import os

from core.base import CustomSnake


def load_scales(bot: CustomSnake):
    """Automatically load all scales in the ./scales folder"""

    bot.logger.info("Loading Scales...")
    # go through all folders in the directory and load the scales from all files
    # Note: files must end in .py
    for root, dirs, files in os.walk("./scales"):
        for file in files:
            if file.endswith(".py") and not file.startswith("__init__"):
                file = file.removesuffix(".py")
                path = os.path.join(root, file)
                python_import_path = path.replace("/", ".").replace("\\", ".")

                # load the scale
                bot.load_extension(python_import_path)

    bot.logger.info(f"< {len(bot.interactions)} > Interactions Loaded")
