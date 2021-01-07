import __token__
import asyncio
import json
import discord
from discord.ext import commands

basic_command_prefix = '/'

def get_command_prefix(bot, msg):
    with open('prefixes.json', 'r') as json_file:
        prefixes = json.loads(json_file)
        if msg.guild.id in prefixes:
            return prefixes[msg.guild.id]
    
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

    open('prefixes.json', 'w').close()

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

if __name__ == '__main__':
    bot.run(__token__.get_token())