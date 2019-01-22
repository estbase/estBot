import asyncio
import socket
import urllib.request
from discord import Embed


def handle(args, message, client, invoke):
    internal_ip = socket.gethostbyname(socket.gethostname())
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return_msg = yield from client.send_message(message.channel, embed=Embed(colour=0x708DD0, description=(
        "Pong!")))
    yield from client.send_message(message.author,
                                   "You internal IP is: " + internal_ip + "\nYour external IP is: " + external_ip)
    yield from asyncio.sleep(5)
    yield from client.delete_message(return_msg)
