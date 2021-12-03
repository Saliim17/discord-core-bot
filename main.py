import discord
import os
from discord import reaction
from discord.message import Message
from dotenv import load_dotenv
load_dotenv()
import random
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio

client = discord.Client()

algorithm = ["algoritmica"]
ac = ["ac", "arquitectura", "arquitectura de computadores"]
baco_ailajas = ["paco", "aylagas", "paco aylagas", "Paco", "Aylagas", "Paco Aylagas", "PACO", "AYLAGAS", "PACO AYLAGAS"]
suspender = ["suspender", "suspenso", "suspendo", "suspendería", "he suspendido", "suspendió"]
mejor = ["mejor", "makina", "bueno"]
starter_algorithms = [
    "Nah, algorítimica está chupado. Yo saqué un 9. 😁",
    "Algorítmica es imposible de aprobar. 😢",
    "Backtracking 🤪"
]
starter_ac = [
    "Nah, AC es fácil lo que pasa es que no estudias.😈",
    "Yo no se ni lo que es un fetch. 😴",
    "Forwarding 🥴"
]
starter_paco = [
    "Paco Aylagas es el mejor profesor de la ETSISI. ❤️‍🔥",
    "Quién no conoce a Paco a cualquier Miñano le reza. :palms_up_together:"
]

ayuda = ["help", "ayuda"]
bot = ["bot", "Coru", "coru"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # If the author of the message is bot, we do nothing.
    if message.author == client.user:   
        return

    msg = message.content
    #if msg.startswith(''):
     #   await message.channel.send('Hello!')

    if any(word in msg for word in ayuda) or any(word in msg for word in bot):
        msg1 = await message.channel.send("Select language:")
        await client.add_reaction(msg1, ":flag_es:")
    if any(word in msg for word in algorithm) and any(word in msg for word in suspender):
        await message.channel.send(random.choice(starter_algorithms))

    if any(word in msg for word in ac) and any(word in msg for word in suspender):
        await message.channel.send(random.choice(starter_ac))

    if any(word in msg for word in baco_ailajas) and any(word in msg for word in mejor):
        await message.channel.send(random.choice(starter_paco))


client.run(os.getenv("BOT_TOKEN"))
