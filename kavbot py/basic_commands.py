
import discord
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from discord import client


def run_bot(client):
<<<<<<< HEAD
    pre_commands = {'what is ':'Definitions from the dictionary',
                    'hi':'Returns  Hi Ho',
                    'music':'Try it'
                    ,'time':'Returns current time'}
=======
    pre_commands = {'what is ':' Returns Definitions from the dictionary',
                    'hi':' Returns Hi Ho',
                    'music':' Try it'
                    ,'time':' Returns current time'}
>>>>>>> 7466d550a3cc0bcf30dd48e3cc33d59a40a8bf6f
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
                                        

            elif command.startswith('hi'):
                await message.channel.send("Hi Ho")

            elif command.startswith('music'):
                await message.channel.send("What music, use rythm")

            elif command.startswith('time'):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                await message.channel.send(current_time)
            elif command.startswith('join'):

                if (ctx.author.voice):
                    channel=ctx.message.author.voice.channel
                    await channel.connect()
                else :
                    await ctx.send( "Please join a voice channel" )

            else:
                await message.channel.send("The command "+ command + " not available")
                await message.channel.send("Commands that are avalaible")
                for i in pre_commands:
                    await message.channel.send(i+pre_commands[i])
