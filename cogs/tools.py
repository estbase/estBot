import asyncio

import datetime
import discord
import json
import pytz as pytz
import random
import requests
from discord import Embed
from discord.ext import commands


class Tools:
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
                    return_msg = await self.bot.say(embed=Embed(colour=0x708DD0, description=(
                        "Sending the information to you by private message!")))
                    await self.bot.send_message(ctx.message.author, out)
                    await asyncio.sleep(5)
                    await ctx.bot.delete_message(return_msg)
                elif resp['status'] == 'fail':
                    self.bot.send_message(ctx.message.author, 'API Request Failed')
            else:
                await self.bot.say('HTTP Request Failed: Error {}'.format(req.status_code))
        except Exception as e:
            print(e)

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

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, args: int):
        '''Delete N messages from channel.'''
        try:
            amount = int(args) + 1 if int(args) > 0 else 2
        except:
            await self.bot.say(
                embed=Embed(color=discord.Color.red(), descrition="Please enter a valid value for message amount!"))
            return

        messages = []
        async for m in self.bot.logs_from(ctx.message.channel, limit=amount):
            messages.append(m)
        await ctx.bot.delete_messages(messages)
        return_msg = await self.bot.say(
            embed=discord.Embed(colour=0x708DD0,
                                description="Successfully cleared `%s message(s)`. :ok_hand:" % (amount - 1)))
        await asyncio.sleep(5)
        await ctx.bot.delete_message(return_msg)

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong! Returns your websocket latency."""
        t = await self.bot.say('Pong!')
        ms = (t.timestamp - ctx.message.timestamp).total_seconds() * 1000
        await self.bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

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
                return await self.bot.say(embed=em)
            await self.bot.say(f'**{tz}:** It is currently {now:%A, %B %d, %Y} at {now:%I:%M:%S %p}.')
        else:
            await self.bot.say(f'**EST Base Headquarters:** It is currently {now:%A, %B %d, %Y} at {now:%I:%M:%S %p}.')
            await self.bot.say(f'**UTC Time:** It is currently {utctime:%A, %B %d, %Y} at {utctime:%I:%M:%S %p}.')


def setup(bot):
    bot.add_cog(Tools(bot))
