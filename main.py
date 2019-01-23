import asyncio
import inspect
import os
import json
from discord import Game
from discord.ext import commands

# Definitions
config = json.loads(open('settings/config.json').read())
extensions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
path = config['cogs_path']
client = commands.Bot(command_prefix=config['prefix'])

print('Extensiones disponibles: ')
print(extensions)
print()


@client.command()
async def load(extension):
    try:
        client.load_extension(path+'.'+extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))


@client.command()
async def unload(extension):
    try:
        client.unload_extension(path+'.'+extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))


client.remove_command('help')


# When BOT is ready
@client.event
@asyncio.coroutine
def on_ready():
    try:
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        print('Bot is logged in successfully. Running on servers: ' + str(len(client.servers)))
        for s in client.servers:
            print(" - %s (%s)" % (s.name, s.id))
        yield from client.change_presence(game=Game(name="Testing BOT | " + config['version']))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(path+'.'+extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

    client.run(config['token'])
