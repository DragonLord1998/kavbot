
import discord
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from discord import client


def run_bot(client):
    
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
                                        

            if command.startswith('hi'):
                await message.channel.send("Hi Ho")

            if command.startswith('music'):
                await message.channel.send("What music, use rythm")

            if command.startswith('time'):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                await message.channel.send(current_time)