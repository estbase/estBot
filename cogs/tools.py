import random
from discord.ext import commands


class Tools:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description="Returning all info about network from user")
    async def ip(self, ctx):
        await self.bot.send_message(ctx.message.author, "test")
        await self.bot.say('Ni IP ni ostias.')

    @commands.command()
    async def roll(self, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
            if rolls <= 0:
                await self.bot.say('You can choose at least 1 roll')
                return
        except Exception as error:
            await self.bot.say('Format has to be in NdN!')
            print('Some error has been occurred on rolls a dice. ERROR: {}'.format(error))
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(result)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, *choices: str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))


def setup(bot):
    bot.add_cog(Tools(bot))
