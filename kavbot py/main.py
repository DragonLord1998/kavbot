#main

import json
import discord
import os
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from discord import channel
from basic_commands import commands_loop
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client()
bot = commands.Bot(command_prefix="$kb",intents = intents)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@bot.event
async def on_message(message):
    # do some extra stuff here
    await message.channel.send("This works - bot event")
    await bot.process_commands(message)
#commands_loop(client,bot)


client.run(os.environ.get("TOKEN"))

