import asyncio
import json
import discord
from discord import Game, Embed, Color
from commands import cmd_ping, cmd_ip, cmd_clear, cmd_userinfo, cmd_help

config = json.loads(open('settings/config.json').read())
BOT_PREFIX = ('!', '-')

client = discord.Client()


commands = {
    "ping": cmd_ping,
    "ip": cmd_ip,
    "clear": cmd_clear,
    'userinfo': cmd_userinfo,
    'help': cmd_help,
}


# When BOT is ready
@client.event
@asyncio.coroutine
def on_ready():
    try:
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        print('Bot is logged in successfully. Running on servers: \n')
        for s in client.servers:
            print(" - %s (%s)" % (s.name, s.id))
        yield from client.change_presence(game=Game(name="Testing BOT"))
    except Exception as e:
        print(e)


# When receive a new message
@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(BOT_PREFIX):
        invoke = message.content[1:].split(" ")[0]
        args = message.content.split(" ")[1:]
        print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()))
        if commands.__contains__(invoke):
            yield from commands.get(invoke).handle(args, message, client, invoke)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=("The command '%s' is not valid!" % invoke)))


client.run(config['token'])
