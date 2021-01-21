from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self, ctx):
        '''To develop. Future command to improve the default info command.'''
        await ctx.send('This channel is property of {} and this moment is under development.'.format(ctx.message.server.owner))

    @commands.command()
    async def invite(self, ctx):
        '''Invite the bot to your server'''
        await ctx.send(
            f"Invite me to your server: https://discordapp.com/oauth2/authorize?client_id=536867877702205450&scope=bot&permissions=268905542"
        )


def setup(bot):
    bot.add_cog(Help(bot))
