import asyncio
import json
import requests
from discord import Embed


def handle(args, message, client, invoke):
    channel = message.channel
    try:
        req = requests.get('http://ip-api.com/json/')
        resp = json.loads(req.content.decode())
        if req.status_code == 200:
            if resp['status'] == 'success':
                out = '**Your data:**\n**IP: ** ' + resp['query'] + '\n**City: **' + resp['city'] + '\n**State: **' + \
                      resp['regionName'] + '\n**Country: **' + resp['country'] + '\n**Latitude: **' + str(resp[
                          'lat']) + '\n**Longitude: **' + str(resp['lon']) + '\n**ISP: **' + resp['isp']
                return_msg = yield from client.send_message(channel, embed=Embed(colour=0x708DD0, description=(
                            "Sending the information to you by private message!")))
                yield from client.send_message(message.author, out)
                yield from asyncio.sleep(5)
                yield from client.delete_message(return_msg)
            elif resp['status'] == 'fail':
                yield from client.send_message(message.author, 'API Request Failed')
        else:
            yield from client.send_message(channel, 'HTTP Request Failed: Error {}'.format(req.status_code))
    except Exception as e:
        print(e)
