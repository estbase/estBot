import asyncio
import datetime
import discord
import json
import pytz as pytz
import random
import requests
from discord import Embed
from discord.ext import commands


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description="Returning all info about network from user")
    async def ip(self, ctx):
        '''Returns a information from user network.

        IP, City, State, Country, ISP, and Long & Lat from your connection.
        '''
        try:
            req = requests.get('http://ip-api.com/json/')
            resp = json.loads(req.content.decode())
            if req.status_code == 200:
                if resp['status'] == 'success':
                    out = '**Your data:**\n**IP: ** ' + resp['query'] + '\n**City: **' + resp[
                        'city'] + '\n**State: **' + \
                          resp['regionName'] + '\n**Country: **' + resp['country'] + '\n**Latitude: **' + str(resp[
                                                                                                                  'lat']) + '\n**Longitude: **' + str(
                        resp['lon']) + '\n**ISP: **' + resp['isp']
                    return_msg = await ctx.send(embed=Embed(colour=0x708DD0, description=(
                        "Sending the information to you by private message!")))
                    await self.bot.send_message(ctx.message.author, out)
                    await asyncio.sleep(5)
                    await ctx.bot.delete_message(return_msg)
                elif resp['status'] == 'fail':
                    self.bot.send_message(ctx.message.author, 'API Request Failed')
            else:
                await ctx.send('HTTP Request Failed: Error {}'.format(req.status_code))
        except Exception as e:
            print(e)

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
            if rolls <= 0:
                await ctx.send('You can choose at least 1 roll')
                return
        except Exception as error:
            await ctx.send('Format has to be in NdN!')
            print('Some error has been occurred on rolls a dice. ERROR: {}'.format(error))
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, args: int):
        '''Delete N messages from channel.'''
        try:
            amount = int(args) + 1 if int(args) > 0 else 2
        except:
            await ctx.send(
                embed=Embed(color=discord.Color.red(), descrition="Please enter a valid value for message amount!"))
            return

        messages = []
        async for m in ctx.message.channel.history(limit=amount):
            messages.append(m)
        await ctx.message.channel.delete_messages(messages)
        return_msg = await ctx.send(
            embed=discord.Embed(colour=0x708DD0,
                                description="Successfully cleared `%s message(s)`. :ok_hand:" % (amount - 1)),
            delete_after=5)

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong! Returns your websocket latency."""
        t = await ctx.send('Pong!')
        ms = (t.created_at - ctx.message.created_at).total_seconds() * 1000
        await t.edit(content='Pong! Took: {}ms'.format(int(ms)))

    @commands.command(pass_context=True)
    async def datetime(self, ctx, tz=None):
        """Get the current date and time for a time zone or UTC."""
        now = datetime.datetime.now(tz=pytz.timezone('Europe/Madrid'))
        utctime = datetime.datetime.now(tz=pytz.UTC)
        all_tz = 'https://github.com/estbase/estBot/blob/master/settings/timezones.json'
        if tz:
            try:
                now = now.astimezone(pytz.timezone(tz))
            except:
                em = discord.Embed(color=discord.Color.red())
                em.title = "Invalid timezone"
                em.description = f'Please take a look at the [list]({all_tz}) of timezones.'
                return await ctx.send(embed=em)
            await ctx.send(f'**{tz}:** It is currently {now:%A, %B %d, %Y} at {now:%I:%M:%S %p}.')
        else:
            await ctx.send(f'**EST Base Headquarters:** It is currently {now:%A, %B %d, %Y} at {now:%I:%M:%S %p}.')
            await ctx.send(f'**UTC Time:** It is currently {utctime:%A, %B %d, %Y} at {utctime:%I:%M:%S %p}.')


def setup(bot):
    bot.add_cog(Tools(bot))
