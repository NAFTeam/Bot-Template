from core.base import CustomSnake

from dis_snek import InteractionContext, Scale, slash_command


class CommandScale(Scale):
    bot: CustomSnake

    @slash_command(name="hello_world", description="My first command :)")
    async def my_command(self, ctx: InteractionContext):
        """Says hello to the world"""

        await ctx.send("Hello World")


def setup(bot: CustomSnake):
    """Let dis-snek load the scale"""

    CommandScale(bot)
