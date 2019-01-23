import asyncio
import json
import requests
from discord import Embed
from discord.ext import commands


class Tools:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ip(self):
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
                    return_msg = await self.client.say(self.client.channel, embed=Embed(colour=0x708DD0, description=("Sending the information to you by private message!")))
                    await self.client.say(self.client.message.author, out)
                    await asyncio.sleep(5)
                    await self.client.delete_message(return_msg)
                elif resp['status'] == 'fail':
                    await self.client.say(self.client.message.author, 'API Request Failed')
            else:
                await self.client.say(self.client.channel, 'HTTP Request Failed: Error {}'.format(req.status_code))
        except Exception as e:
            print(e)


def setup(client):
    client.add_cog(Tools(client))
