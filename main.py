import asyncio

import logging
import os
import json
import traceback
from discord import Game
from discord.ext import commands

# Definitions
config = json.loads(open('settings/config.json').read())
extensions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
path = config['cogs_path']
bot = commands.Bot(command_prefix=config['prefix'])

print('Extensiones disponibles: ')
print(extensions)
print()


@bot.command()
async def load(extension):
    '''Load an extension.'''
    try:
        bot.load_extension(path+'.'+extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))


@bot.command()
async def unload(extension):
    '''Unload an extension.'''
    try:
        bot.unload_extension(path+'.'+extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))


# bot.remove_command('help')


# When BOT is ready
@bot.event
async def on_ready():
    try:
        await load_cogs()
        await bot.change_presence(game=Game(name="Testing BOT | " + config['version']))
        print('\nBot logged in as ' + bot.user.name + ' with ID: ' + bot.user.id)
        print('------')
        print('Bot is logged in successfully. Running on servers: ' + str(len(bot.servers)))
        for s in bot.servers:
            print(" - %s (%s)" % (s.name, s.id))
    except Exception as e:
        print(e)


async def load_cogs():
    '''Load automatically all cogs found on folder'''
    for extension in extensions:
        try:
            print('Loading {}...'.format(extension))
            bot.load_extension(path+'.'+extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
            traceback.print_exc()


def main():
    logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    main()

    bot.run(config['token'])
