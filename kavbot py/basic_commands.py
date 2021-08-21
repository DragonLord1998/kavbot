from PyDictionary import PyDictionary as dictionary
import discord
from datetime import datetime
from discord import message
from discord.ext import commands
from commands import commands_kav 
from dictionaries import dict
from qotd import quotes
from weather import weather

def commands_loop(client,bot):
    pre_commands = commands_kav()
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
            elif command.startswith('quote'):
                quote = quotes()
                await message.channel.send(quote)
                return None
                

            elif command.startswith('meaning'):
                words=message.content.split("meaning")
                ans = dict(words[1])
                
                await message.channel.send("Meaning: " +ans['meaning'])
                await message.channel.send("Example: " +ans['example'])

                return None

            elif command.startswith('music'):
                await message.channel.send("What music, use rythm")
                return None
            
            elif command.startswith('weather'):
                words=message.content.split("weather")
                climate = weather(words[1])
                await message.channel.send("Current Temperature of "+ climate['city_name'] + "is :"+ climate["temp"])
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

    @bot.command(pass_context = True)
    async def join(ctx):
        print("tHIS WORKS")
        await message.channel.send( "command runs" )



