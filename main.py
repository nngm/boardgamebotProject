import asyncio
import logger
import json

import discord
from discord.ext import commands

import __token__

basic_command_prefix = '/'
bot_name = 'BoardGameBot'
bot_initial = 'BGB'
prefix_file_name = 'prefixes.json'
help_command = basic_command_prefix + 'help'
prefixes = {}

def get_help_message(message) -> str:
    server_id = str(message.guild.id)

    # if message.content == help_command
    if server_id in prefixes:
        descr = f'Prefix for this server is `{prefixes[server_id]}`'
    else:
        descr = f'Prefix for this server is `{basic_command_prefix}`'
    # descr += all commands explanation
    return descr

bot = commands.Bot(
    command_prefix=lambda bot, message: prefixes[str(message.guild.id)] 
        if str(message.guild.id) in prefixes else basic_command_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    global prefixes

    # custom activity for bots are not available now
    activity_name = f'{bot_initial} | Use {help_command} ' + \
                     'to get current prefix and commands.'
    await bot.change_presence(activity=discord.Game(activity_name))

    try:
        with open(prefix_file_name, 'r') as json_file:
            if json_file.read() == '':
                raise FileNotFoundError
    except FileNotFoundError:
        with open(prefix_file_name, 'w') as json_file:
            json_file.write(json.dumps({}))
        print('Empty "prefixes.json" file made.')
    
    with open(prefix_file_name, 'r') as json_file:
        prefixes = json.loads(json_file.read())

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        return
    raise error

@bot.command()
async def ping(ctx):    # ping
    await ctx.send('pong')

@bot.command()
async def prefix(ctx):  # change prefix
    server_id = str(ctx.guild.id)
    
    try:
        new_prefix = ctx.message.content.split()[1]
    except:
        await ctx.send(f'Type `{help_command} prefix` for usage.')
        return
    
    prefixes[server_id] = new_prefix
    
    try:
        with open(prefix_file_name, 'w') as json_file:
            json_file.write(json.dumps(prefixes))
        # raise Exception('Test')
    except Exception as e:
        await ctx.send('Failed to change prefix.')
        logger.log(f'{e}: An exception occurred while changing prefix.')
        logger.log(f'server: {server_id} ({ctx.guild.name})')
        logger.log(f'author: {ctx.author.id} ({ctx.author.name})')
        logger.log(f'used command: {ctx.message.content}')
    else:
        await ctx.send(f'Prefix for this server changed to `{new_prefix}`')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content == help_command or message.content.startswith(help_command + ' '):
        await message.channel.send(get_help_message(message))
    
    await bot.process_commands(message)

@bot.command()
async def 오목(ctx):
    # cmd = {'뜨자': omok.request}
    
    try:
        argv = ctx.message.content.split()


    except:
        await ctx.send(f'Type `{help_command} 오목` for usage.')
        return

if __name__ == '__main__':
    bot.run(__token__.get_token())