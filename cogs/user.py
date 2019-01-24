from discord import Embed
from discord.ext import commands


class User:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def me(self, ctx):
        try:
            user = ctx.message.author
            em = Embed(colour=0x708DD0)
            em.add_field(name='User ID :beginner:', value=user.id, inline=True)
            em.add_field(name='Username :desktop:', value=user, inline=True)
            em.add_field(name='Status :eye:', value=user.status, inline=True)
            em.add_field(name='Highest Role :tools:', value=user.top_role.name, inline=True)
            em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            em.set_footer(text="You can visit us on https://www.estbase.org")
            em.set_author(name="EST Base Discord Bot",
                          icon_url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
            em.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.bot.say(embed=em)
        except Exception as error:
            print("Some error has been occurred on executing User.me. Error: {}".format(error))


def setup(bot):
    bot.add_cog(User(bot))
