from discord.ext import commands


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self, ctx):
        await self.bot.say('This channel is property of {} and this moment is under development.'.format(ctx.message.server.owner))


def setup(bot):
    bot.add_cog(Help(bot))
