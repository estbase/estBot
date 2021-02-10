import discord
import requests
from discord.ext import commands
from json import dumps, loads

config = loads(open('settings/config.json').read())
riotApiKey = config['riot_apiKey']

class GameStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fortnite")
    async def fortnite_stats(self, ctx, name):
        link = await ctx.channel.create_invite(max_uses=0, max_age=0)
        save(ctx.guild.name, ctx.guild.id, link)
        embed = discord.Embed(
            title=f":sparkles: Fortnite Profile: {name}",
            description="Your profile and stats:",
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
                            value=f"Level: {level} | Playtime: {playtime / 60 :.1f}h \n\u200b", inline=False)
            embed.add_field(name='Kills', value=kills, inline=True)
            embed.add_field(name='Deaths', value=deaths, inline=True)
            embed.add_field(name='K/D', value=f"{kd} \n\u200b", inline=True)
            embed.add_field(name='Wins', value=wins, inline=True)
            embed.add_field(name='Matches', value=matches, inline=True)
            embed.add_field(name='Win Rate', value=f"{wr}%", inline=True)
        except:
            pass
        await ctx.send(embed=embed)

    @commands.command(name="lol")
    async def lol_stats(self, ctx, region, name):
        region_key = {"eune": "EUN1", "euw": "EUW1", "jp": "JP1", "kr": "KR", "la": "LA1", "na": "NA1", "oc": "OC1",
                      "ru": "RU", "tr": "TR", "la2": "LA2"}
        api_key = riotApiKey
        link = await ctx.channel.create_invite(max_uses=0, max_age=0)
        save(ctx.guild.name, ctx.guild.id, link)

        try:
            region = region_key[region.lower()]
            response = requests.get(
                f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}")

            json_dump = dumps(response.json())
            json_object = loads(json_dump)

            level = json_object["summonerLevel"]
            unique_id = json_object['id']
            icon_id = json_object['profileIconId']

            response = requests.get(
                f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{unique_id}?api_key={api_key}")
            json_dump = dumps(response.json())
            json_object = loads(json_dump)
            queue = json_object[0]
            icon_id = f"http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/{icon_id}.png"
        except:
            name = "Wrong name or region."
            level = "N\A"
            queue = []
            icon_id = ""

        embed = discord.Embed(
            title=f":sparkles: LoL Profile: {name}",
            description='Your profile and stats:',
            color=discord.Colour.red()
        )
        embed.add_field(name='Level / Region:', value=f"{level} / {region}", inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        # embed.add_field(name='Last Games:', value='Under construction...\n\u200b', inline=True)
        # embed.add_field(name='Top Champions:', value='Under construction...', inline=True)
        # embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name='Ranked Stats:', value=f":{queue['tier'].lower()}: **{queue['tier'].capitalize()} {queue['rank']}** "
                                                    f"\n **{queue['leaguePoints']}LP** / {queue['wins']}W / {queue['losses']}L"
                                                    f"\n Winrate: {queue['wins'] * 100 / (queue['wins'] + queue['losses']) :.1f}%"
                                                    f"\n\u200b", inline=True)
        # embed.add_field(name='Last Game:', value='Under construction... try to get this info soon.', inline=False)
        # embed.add_field(name='Live Game:', value='Under construction...', inline=False)
        embed.set_thumbnail(url=icon_id)

        await ctx.send(embed=embed)

# TODO - Next step, save this into SQLite DB to get statistics & improve more used commands
def save(guild, id, link):
    f = open("servers.txt", "a")
    guild += f" {id} {link}\n"
    f.write(guild)

def setup(bot):
    bot.add_cog(GameStats(bot))
