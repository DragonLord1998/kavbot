import discord
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix = '$tb')

@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.channel.send('Pong!')

@bot.command(pass_context=True)
async def add(ctx, *, arg):
    await ctx.send(arg)
bot.run("ODgwMzc1MzM2MTkyMzIzNTk0.YSdXbA.yv8RsUQ55qz4fTnSU9VW2moFse8")