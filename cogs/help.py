import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx, section=''):
        """To develop. Future command to improve the default info command."""
        if section and not section.isspace():
            # Commands & Tools
            embed_commands = discord.Embed(
                title='Commands & Tools',
                description=' ',
                color=discord.Colour.red()
            )
            embed_commands.add_field(name='`$countdown [seconds] [title]`', value='Show a countdown with the title provided', inline=False)
            embed_commands.add_field(name='`$choose [choice1] [choice2] (other choices are optional)`', value='Chooses between multiple choices', inline=False)
            embed_commands.add_field(name='`$ping`', value='Makes a ping to see the response time of the bot', inline=False) # Maybe this command should be only available for server admins
            embed_commands.add_field(name='`$quickpoll [reason] [option1] [option2] (more options)`', value='Makes a poll quickly', inline=False)
            embed_commands.add_field(name='`$roll [NdN]`', value='Rolls a dice in NdN format: NdN = 1d6', inline=False)
            # Moderate
            embed_moderate = discord.Embed(
                title='Moderation commands',
                description=' ',
                color=discord.Colour.red()
            )
            embed_moderate.add_field(name='`$ban`', value='Bans a member from the server', inline=False)
            embed_moderate.add_field(name='`$clear`', value='Clears messages in a channel', inline=False)
            embed_moderate.add_field(name='`$kick`', value='Kicks a member from the server', inline=False)
            # Info
            embed_info = discord.Embed(
                title='Information commands',
                description='General Information',
                color=discord.Colour.red()
            )
            embed_info.add_field(name='`$datetime (time/zone optional)`', value='Provides current date and time for a time zone and UTC', inline=False)
            embed_info.add_field(name='`$me`', value='Send in private, information about user has requested', inline=False)
            embed_info.add_field(name='`$help`', value='Show a list of commands to give help', inline=False)
            embed_info.add_field(name='`$invite`', value='Show a link to invite Bot to your server', inline=False)
            embed_info.add_field(name='`$ip`', value='Sends a private message with all info about your IP', inline=False)
            switch = {
                "commands": embed_commands,
                "moderate": embed_moderate,
                "info": embed_info
            }
            await ctx.send(embed=switch.get(section))
        else:
            em = discord.Embed(
                title='UNDER DEVELOPMENT',
                description='This Discord Bot is actually under development you can contibute or read more info [HERE]('
                            'https://github.com/estbase/estBot)',
                colour=discord.Colour.red()
            )
            em.add_field(name='Commands', value='`$help commands`', inline=True)
            em.add_field(name='Moderator', value='`$help moderate`', inline=True)
            em.add_field(name='About', value='`$help info`', inline=True)

            em.set_footer(text="You can visit us on https://www.estbase.org for more information.")
            em.set_author(name="EST Base Discord Bot",
                          icon_url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
            em.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=em)

    @commands.command()
    async def invite(self, ctx):
        """Invite the bot to your server"""
        await ctx.send(
            f"Invite me to your server: https://discordapp.com/oauth2/authorize?client_id=536867877702205450&scope=bot&permissions=268905542"
        )

    @commands.command()
    async def info(self, ctx):
        """Information about the Bot"""
        members = channels = 0
        for guild in self.bot.guilds:
            members += guild.member_count
            channels += len(guild.text_channels)

        em = discord.Embed(
            description='I\'m a **Electronic Sports Tournaments Base Bot** that provides some **useful commands** to '
                        'manage your own community or team. With expectations of create a **great community** around'
                        ' **eSports**.',
            colour=discord.Colour.red()
        )
        em.add_field(name='Info', value='**Developer:** Anthrax#0558 \n **Website:** **[estbase.org](https://www.estbase.org)** \n **Official server:** **[discord.gg/DpEKAch](https://discord.gg/DpEKAch)**', inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name='Stats', value=f'**Servers:** `{len(self.bot.guilds)}` \n **Users:** `{members}` \n **Channels:** `{channels}`', inline=True)

        em.set_footer(text="Like the project? Colaborate with us!")
        em.set_author(name="EST Base Discord Bot",
                      icon_url='https://cdn.discordapp.com/avatars/536867877702205450/7a612de5dcce089db07e4d18799b013b.png')
        em.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Help(bot))
