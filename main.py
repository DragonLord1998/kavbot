import discord
import os
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from basic_commands import run_bot

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

run_bot(client)

client.run("ODc3NDU5NzcyNjE2NjIyMTMw.YRy8GA.wkgrn_-dV-zQgRXGkoWJy02dEWE")
