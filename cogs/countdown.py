from discord.ext import commands
import asyncio


class Countdown(commands.Cog):
    '''Countdown timer!'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def countdown(self, ctx, seconds, *, title):
        counter = 0
        try:
            secondint = int(seconds)
            if secondint > 300:
                await ctx.send("I don't think I am allowed to do go above 300 seconds \U0001f914")
                raise BaseException
            if secondint < 0 or secondint == 0:
                await ctx.send("I don't think I am allowed to do negatives \U0001f914")
                raise BaseException
            message = await ctx.send("```css" + "\n" + "[" + title + "]" + "\nTimer: " + seconds + "```")
            while True:
                secondint = secondint - 1
                if secondint == 0:
                    await message.edit(content="```Ended!```")
                    break
                await message.edit(content=("```css" + "\n" + "[" + title + "]" + "\nTimer: {0}```".format(secondint)))
                await asyncio.sleep(1)
            await self.bot.send_message(ctx.message.channel, ctx.message.author.mention + " Your countdown " + "[" + title + "]"  + " Has ended!")
        except ValueError:
            await ctx.send("Must be a number!")


def setup(bot):
    bot.add_cog(Countdown(bot))
