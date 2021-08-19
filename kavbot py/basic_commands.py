
import discord
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from discord import client


def run_bot(client):
    pre_commands = {'what is ':' : Returns Definitions from the dictionary',
                    'hi':' : Returns Hi Ho',
                    'music':' : Try it'
                    ,'time':' : Returns current time'}
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
                await message.channel.send(pre_commands.replace("{","").replace("}",""))

             #   for i in pre_commands:
             #      await message.channel.send(i+pre_commands[i])
