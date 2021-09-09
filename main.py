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
bot = commands.Bot(command_prefix='!')

#OpenJson & load strings
with open('strings.json',) as f:
  stringsQuote = json.load(f)

# Check for login
@bot.event
async def on_ready():
  #guild = client.get_guild(707159521457340466) 
  change_status.start()
  print(f'{bot.user.name} has connected to Discord!')



# Check for new user connecting
# @client.event
# async def on_member_join(member):
#   await member.create_dm()
#   await memeber.dm_channel.send(f'{customFromString(stringsQuote["HBB_activity_quote"])}, en somme, bienvenu(e) {member.name}!')

# Change status every minute or so
# tasks.loop(seconds=60)
# async def change_status():
#   await client.change_presence(activity=discord.Game(choice(stringsQuote["HBB_activity_quote"])))
#   print("Changing activity")


# Check for a message in chat. If the message is equal to a command name then 
# we run the code.
@bot.command(name="oss", help="Réponds une citation aléatoire des films OSS17. Attention, les citations d'\"Alerte rouge en Afrique noire\" n'ont pas été ajoutées!")
async def cmdOSSMsg(ctx):
  quoteArr = customFromString(stringsQuote["HBB_quote"])
  for quoteLine in quoteArr:
      print(quoteLine)
      await ctx.send(quoteLine)

@bot.command(name="quote", help="Affiche une citation aléatoire grâce à une API douteuse (https://zenquotes.io/api/random)")
async def cmdQuoteMsg(ctx):
    quote = get_quote()
    await ctx.send(quote)

@bot.command(name="vous savez quoi")
async def cmdVSQMsg(ctx):
    await ctx.send(stringsQuote["vsq"][0])

@bot.command(name="kamoulox", help="Jouez au kamoulox en affichant une phrase construite semi-aléatoirement")
async def cmdKamouloxMsg(ctx):
    phraseTotal = ""
    kamouloxPhrases = customFromString(stringsQuote["kamouloxPhrases"])
    for kamouloxLine in kamouloxPhrases:
      kamouloxMots = customFromString(stringsQuote["KamouloxMots"])
      phraseTotal+=kamouloxLine+ " " +kamouloxMots+ " "
    await ctx.send(phraseTotal)

  #Debug commands
@bot.command(name='err.log', help="DEVELOPPEUR ONLY: Affiche le fichier de log err.log")
async def cmdDebugErrLogMsg(ctx):
    with open('err.log', 'r') as f:
      await ctx.send(f)

keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))