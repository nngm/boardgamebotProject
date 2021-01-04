import __token__
import asyncio
import discord
from discord.ext import commands

command_prefix = '/'
bot = commands.Bot(command_prefix=command_prefix)

# def console_input():
#     while True:
#         s = input()
#         if s.lower() == 'token':
#             print(__token__.get_token())
#         if s.lower() == 'stop':
#             return

@bot.event
async def on_ready():
    activity = discord.CustomActivity('basic prefix is ' + command_prefix)
    await bot.change_presence(activity=activity)    # not working now
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # await console_input()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

async def main():
    bot.run(__token__.get_token())

if __name__ == "__main__":
    asyncio.run(main())