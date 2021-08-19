import discord
import os
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from discord import channel
from discord.flags import Intents
from basic_commands import run_bot
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client()
bot = commands.Bot(command_prefix="$kb",intents = intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


run_bot(client)

@bot.command(pass_context= True)
async def join(ctx):
  if (ctx.author.voice):
    channel=ctx.message.author.voice.channel
    await channel.connect()
  else :
    await ctx.send( "Please join a voice channel" )

@bot.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
    await ctx.send ("I left the voice channel")
  else :
    ctx.send("I am not in a voice channel")

client.run("ODc3NDU5NzcyNjE2NjIyMTMw.YRy8GA.wkgrn_-dV-zQgRXGkoWJy02dEWE")
client.run(os.environ.get("TOKEN"))

