import discord
import os
client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$kb'):
    await message.channel.send("Hi Ho")

  if message.content.startswith('$music'):
    await message.channel.send("What music, use rythm")


client.run("ODc3NDU5NzcyNjE2NjIyMTMw.YRy8GA.wkgrn_-dV-zQgRXGkoWJy02dEWE")
