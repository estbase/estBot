from discord.ext import commands


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pong(self):
        await self.bot.say('Ping!')


def setup(bot):
    bot.add_cog(Help(bot))
