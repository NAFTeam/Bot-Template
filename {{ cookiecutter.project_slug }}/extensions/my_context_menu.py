from core.base import CustomClient

from naff import CommandTypes, InteractionContext, Message, context_menu, Extension


class ContextMenuExtension(Extension):
    bot: CustomClient

    @context_menu(name="repeat", context_type=CommandTypes.MESSAGE)
    async def my_context_menu(self, ctx: InteractionContext):
        """Repeat the message on which the context menu was used"""

        message: Message = ctx.target
        await ctx.send(message.content)


def setup(bot: CustomClient):
    """Let naff load the extension"""

    ContextMenuExtension(bot)
