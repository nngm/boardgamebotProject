import asyncio
import time
import json

import discord
from discord.ext import commands

import __token__

basic_command_prefix = '/'
bot_name = 'BoardGameBot'
bot_initial = 'BGB'

def get_command_prefix(bot, message):
    server_id = str(message.guild.id)
    with open('prefixes.json', 'r') as json_file:
        prefixes = json.loads(json_file.read())
        if server_id in prefixes:
            return prefixes[server_id]
    
    return basic_command_prefix

bot = commands.Bot(command_prefix=get_command_prefix)

@bot.event
async def on_ready():
    # custom activity for bots are not available now
    activity = discord.Game(bot_initial + ' | Use /help to get current prefix and commands.')
    await bot.change_presence(activity=activity)

    try:
        with open('prefixes.json', 'r') as json_file:
            if json_file.read() == '':
                raise FileNotFoundError
    except FileNotFoundError:
        with open('prefixes.json', 'w') as json_file:
            json_file.write(json.dumps({}))
            print('Empty "prefixes.json" file made.')

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):    # ping
    await ctx.send('pong')

@bot.command()
async def prefix(ctx):  # change prefix
    server_id = str(ctx.guild.id)
    new_prefix = ctx.message.content.split()[1]

    with open('prefixes.json', 'r') as json_file:
        prefixes = json.loads(json_file.read())
    
    prefixes[server_id] = new_prefix
    
    try:
        with open('prefixes.json', 'w') as json_file:
            json_file.write(json.dumps(prefixes))
        # raise Exception('Test')
    except Exception as e:
        await ctx.send('Failed to change prefix.')
        print(str(e) + ': An exception occurred while changing prefix.')
        print('local time:', time.strftime('%c', time.localtime(time.time())))
        print('server id:', server_id)
        print('server name:', ctx.guild.name)
        print('author id:', ctx.author.id)
        print('author name:', ctx.author.name)
        print('new prefix:', new_prefix)
        print('full command:', ctx.message.content)
    else:
        await ctx.send('Prefix for this server changed to `' + new_prefix + '`')

if __name__ == '__main__':
    bot.run(__token__.get_token())