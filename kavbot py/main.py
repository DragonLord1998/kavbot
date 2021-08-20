#main
import asyncio
import json
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

pre_commands = {
                    'what is <term>':'  Returns Definitions of term from the dictionary',
                    'hi':'  Returns Hi Ho',
                    'music':'  Try it',
                    'time':'  Returns current time'
                   }
pre_commands = json.dumps(pre_commands, indent=0)
@client.event    
async def on_message(message):
    if message.author == client.user:
        return
        
    if "$kb" in message.content:
        command = message.content.split("$kb ")[1]
        if "what is " in command:
            words=message.content.split("what is ") 
            noun = dictionary.meaning(words[1])["Noun"][0].replace("(","") 
            await message.channel.send("Noun : "+ noun)
            return None
                                    

        elif command.startswith('hi'):
            await message.channel.send("Hi Ho")
            return None

        elif command.startswith('music'):
            await message.channel.send("What music, use rythm")
            return None

        elif command.startswith('time'):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await message.channel.send(current_time)
            return None

        elif command.startswith('join'):

            if (ctx.author.voice):
                channel=ctx.message.author.voice.channel
                await channel.connect()
            else :
                await ctx.send( "Please join a voice channel" )
        if command.startswith('get message'):
            await message.channel.send(message)

        else:
            await message.channel.send("The command "+ command + " not available")
            await message.channel.send("Commands that are avalaible: ")
            ans = str(pre_commands).replace("{","").replace("}","").replace('"',"").replace(",","")
            await message.channel.send(ans)
    await bot.process_commands(message) 



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

client.run(os.environ.get("TOKEN"))

