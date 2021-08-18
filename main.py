import discord
import os
from datetime import datetime
from PyDictionary import PyDictionary as dictionary

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if "what is " in message.content:
    words=message.content.split("what is ")
    await message.channel.send(dictionary.meaning(words[1]))

  if message.content.startswith('$kb'):
    await message.channel.send("Hi Ho")

  if message.content.startswith('$music'):
    await message.channel.send("What music, use rythm")

  if message.content.startswith('$time'):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await message.channel.send(current_time)


client.run("ODc3NDU5NzcyNjE2NjIyMTMw.YRy8GA.wkgrn_-dV-zQgRXGkoWJy02dEWE")
