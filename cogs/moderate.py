import discord
from discord.ext import commands


class Modetare(commands.Cog):
    """Moderation system."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a member from a server.

        You can kick a member from the server sending or not a reason"
        """
        await member.kick(reason=reason)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban a member from a server.

        You can ban a member from the server sending or not a reason"
        """
        await member.ban(reason=reason)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, args: int):
        """Delete N messages from channel."""
        try:
            amount = int(args) + 1 if int(args) > 0 else 2
        except:
            await ctx.send(
                embed=discord.Embed(color=discord.Color.red(),
                                    description="Please enter a valid value for message amount!"))
            return

        await ctx.channel.purge(limit=amount)
        await ctx.send(
            embed=discord.Embed(colour=discord.Colour.red(),
                                description="Successfully cleared `%s message(s)`. :ok_hand:" % (amount - 1)),
            delete_after=5)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please pass in all required arguments')

def setup(bot):
    bot.add_cog(Modetare(bot))
