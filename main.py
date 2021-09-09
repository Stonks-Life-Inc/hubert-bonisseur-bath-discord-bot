# Hubert Bonisseur de La Bath BOT pour discord
# Ajoute des commandes de toute sorte pour la rigolade.

# A propos de Hubert Bonisseur de la Bath

# Hubert Bonisseur de La Bath, alias OSS 117, est un agent secret

import os
import discord
from discord.ext import tasks, commands
from keep_alive import keep_alive

import json

from globalDef import *

# INIT
client = discord.Client()

#OpenJson & load strings
with open('strings.json',) as f:
  stringsQuote = json.load(f)

# Check for login
@client.event
async def on_ready():
  #guild = client.get_guild(707159521457340466) 
  change_status.start()
  print(f'{client.user} has connected to Discord!')

# Check for new user connecting
# @client.event
# async def on_member_join(member):
#   await member.create_dm()
#   await memeber.dm_channel.send(f'{customFromString(stringsQuote["HBB_activity_quote"])}, en somme, bienvenu(e) {member.name}!')

# Change status every minute or so
tasks.loop(seconds=60)
async def change_status():
  await client.change_presence(activity=discord.Game(choice(stringsQuote["HBB_activity_quote"])))
  print("Changing activity")


# Check for a message in chat. If the message is equal to a command name then 
# we run the code.
@client.event
async def on_message(message):
  #Otpimization, ignoring self messages
  if message.author == client.user:
    return

  if "oss" == message.content.lower():
    quoteArr = customFromString(stringsQuote["HBB_quote"])
    for quoteLine in quoteArr:
      print(quoteLine)
      await message.channel.send(quoteLine)
  elif "quote" == message.content.lower():
    quote = get_quote()
    await message.channel.send(quote)
  elif "vous savez quoi" == message.content.lower():
    await message.channel.send(stringsQuote["vsq"][0])
  elif "kamoulox" == message.content.lower():
    phraseTotal = ""
    kamouloxPhrases = customFromString(stringsQuote["kamouloxPhrases"])
    for kamouloxLine in kamouloxPhrases:
      kamouloxMots = customFromString(stringsQuote["KamouloxMots"])
      phraseTotal+=kamouloxLine+ " " +kamouloxMots+ " "
    await message.channel.send(phraseTotal)

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))