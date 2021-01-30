import discord
import random
import os

from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv('.env')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ola'):
        options = ['Sr.Badcall', 'Palhaço', 'Crewmate', message.author]
        response = "Ola {}".format(random.choice(options))
        await message.channel.send(response)

keep_alive()
client.run(os.getenv('TOKEN'))