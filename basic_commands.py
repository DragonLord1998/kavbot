
import discord
from datetime import datetime
from PyDictionary import PyDictionary as dictionary
from discord import client


def run_bot(client):
    
    @client.event    
    async def on_message(message):
        if message.author == client.user:
            return
        if "what is " in message.content:
            words=message.content.split("what is ")  
            await message.channel.send("Noun : " + dictionary.meaning(words[1])["Noun"][0].replace("(",""))

        if message.content.startswith('$kb'):
            await message.channel.send("Hi Ho")

        if message.content.startswith('$music'):
            await message.channel.send("What music, use rythm")

        if message.content.startswith('$time'):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            await message.channel.send(current_time)
