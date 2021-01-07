import __token__
import asyncio
import json
import discord
from discord.ext import commands

basic_command_prefix = '/'

def get_command_prefix(bot, message):
    server_id = message.guild.id
    with open('prefixes.json', 'r') as json_file:
        prefixes = json.loads(json_file.read())
        if server_id in prefixes:
            return prefixes[server_id]
    
    return basic_command_prefix

# def console_input():
#     while True:
#         s = input()
#         if s.lower() == 'token':
#             print(__token__.get_token())
#         if s.lower() == 'stop':
#             return

bot = commands.Bot(command_prefix=get_command_prefix)

@bot.event
async def on_ready():
    # custom activity for bots are not available now
    activity = discord.Game('basic prefix is ' + basic_command_prefix)
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
async def ping(ctx):
    await ctx.send('pong')

if __name__ == '__main__':
    bot.run(__token__.get_token())