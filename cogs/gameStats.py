import discord
import requests
from discord.ext import commands
from json import dumps, loads


class GameStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fortnite")
    async def fortnite_stats(self, ctx, name):
        link = await ctx.channel.create_invite(max_uses=0, max_age=0)
        save(ctx.guild.name, ctx.guild.id, link)
        embed = discord.Embed(
            title='Fortnite Player Stats',
            color=discord.Colour.red()
        )
        try:
            response = requests.get(f"https://fortnite-api.com/v1/stats/br/v2?name={name}")
            json_dump = dumps(response.json())
            json_object = loads(json_dump)
            overall = json_object["data"]["stats"]["all"]["overall"]

            level = json_object["data"]["battlePass"]["level"]
            wins = overall["wins"]
            kills = overall["kills"]
            deaths = overall["deaths"]
            kd = overall["kd"]
            matches = overall["matches"]
            wr = overall["winRate"]
            playtime = overall["minutesPlayed"]
        except:
            name = "Wrong Name"
            level = "N\A"
            embed = discord.Embed(title=f"{name}   {level} lvl")
        try:
            embed.add_field(name="Overall",
                            value=f"Level: {level} | Playtime: {playtime / 60 :.1f}h", inline=False)
            embed.add_field(name='Kills', value=kills, inline=True)
            embed.add_field(name='Deaths', value=deaths, inline=True)
            embed.add_field(name='K/D', value=kd, inline=True)
            embed.add_field(name='Wins', value=wins, inline=True)
            embed.add_field(name='Matches', value=matches, inline=True)
            embed.add_field(name='Win Rate', value=wr+'%', inline=True)
        except:
            pass
        await ctx.send(embed=embed)

# TODO - Next step, save this into SQLite DB to get statistics & improve more used commands
def save(guild, id, link):
    f = open("servers.txt", "a")
    guild += f" {id} {link}\n"
    f.write(guild)

def setup(bot):
    bot.add_cog(GameStats(bot))
