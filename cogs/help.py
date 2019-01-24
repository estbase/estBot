from discord.ext import commands


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self):
        await self.bot.say('Util information. TBD (To Be Developed)')


def setup(bot):
    bot.add_cog(Help(bot))
