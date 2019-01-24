import discord
from discord.ext import commands


def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)


class Polls:
    """Poll voting system."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def quickpoll(self, ctx, *questions_and_choices: str):
        """Makes a poll quickly.

        The first argument is the question and the rest are the choices.
        You can type phrases writing "This is an example"
        """
        channel = discord.Channel

        if len(questions_and_choices) < 3:
            return await self.bot.say('Need at least 1 question with 2 choices.')
        elif len(questions_and_choices) > 21:
            return await self.bot.say('You can only have up to 20 choices.')

        perms = channel.permissions_for(ctx.message.channel, ctx.message.author)
        if not (perms.read_message_history or perms.add_reactions):
            return await self.bot.say('Need Read Message History and Add Reactions permissions.')

        question = questions_and_choices[0]
        choices = [(to_emoji(e), v) for e, v in enumerate(questions_and_choices[1:])]

        try:
            await ctx.bot.delete_message(ctx.message)
        except:
            pass

        body = "\n".join(f"{key}: {c}" for key, c in choices)
        poll = await self.bot.say(f'{ctx.message.author.name} asks: {question}\n\n{body}')
        for emoji, _ in choices:
            await self.bot.add_reaction(poll, emoji)


def setup(bot):
    bot.add_cog(Polls(bot))
