from core.base import CustomSnake

from dis_snek import (
    Button,
    ButtonStyles,
    ComponentContext, Embed,
    InteractionContext,
    Scale,
    component_callback, slash_command,
)


class CommandScale(Scale):
    bot: CustomSnake

    @slash_command(name="hello_world", description="My first command :)")
    async def my_command(self, ctx: InteractionContext):
        """Says hello to the world"""

        # adds a component to the message
        components = Button(
            style=ButtonStyles.GREEN,
            label="Hiya",
            custom_id="hello_world_button"
        )

        # adds an embed to the message
        embed = Embed(title="Hello World 2", description="Now extra fancy")

        # respond to the interaction
        await ctx.send("Hello World", embeds=embed, components=components)


    @component_callback("hello_world_button")
    async def my_callback(self, ctx: ComponentContext):
        """Callback for the component from the hello_world command"""

        await ctx.send("Hiya to you too")


def setup(bot: CustomSnake):
    """Let dis-snek load the scale"""

    CommandScale(bot)
