import asyncio
import inspect
import os
import json
from discord import Game
from discord.ext import commands

# Definitions
config = json.loads(open('settings/config.json').read())
extensions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
BOT_PREFIX = ('!', '-')
path = config['cogs_path']
client = commands.Bot(command_prefix='-')

print('Extensiones disponibles: ')
print(extensions)
print()


def load_extension(cog, path='cogs.'):
    members = inspect.getmembers(cog)
    for name, member in members:
        if name.startswith('on_'):
            client.add_listener(member, name)
    try:
        client.load_extension(f'{path}{cog}')
    except Exception as e:
        print(f'LoadError: {cog}\n{type(e).__name__}: {e}')


def load_extensions(cogs, path='cogs.'):
    for cog in cogs:
        members = inspect.getmembers(cog)
        for name, member in members:
            if name.startswith('on_'):
                client.add_listener(member, name)
        try:
            client.load_extension(f'{path}{cog}')
        except Exception as e:
            print(f'LoadError: {cog}\n{type(e).__name__}: {e}')


load_extensions(extensions)
client.remove_command('help')
version = "v1.0.0"
test="test"

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
        yield from client.change_presence(game=Game(name="Testing BOT | " + version))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    client.run(config['token'])
