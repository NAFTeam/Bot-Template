from core.base import CustomSnake

from dis_snek import CommandTypes, InteractionContext, Message, Scale, context_menu


class ContextMenuScale(Scale):
    bot: CustomSnake

    @context_menu(name="repeat", context_type=CommandTypes.MESSAGE)
    async def my_context_menu(self, ctx: InteractionContext):
        """Repeat the message on which the context menu was used"""

        message: Message = ctx.target
        await ctx.send(message.content)


def setup(bot: CustomSnake):
    """Let dis-snek load the scale"""

    ContextMenuScale(bot)
