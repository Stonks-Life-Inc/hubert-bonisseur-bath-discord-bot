import asyncio
import functools
import itertools
import math
import random 
from random import choice 
from array import *
import requests
import json
from replit import db

#import yt

import os
import discord
from keep_alive import keep_alive
from discord.ext import commands, tasks
import youtube_dl
from async_timeout import timeout

from discord.ext import commands


client = discord.Client()


@client.event
async def on_ready():
  change_status.start()
  print('We have logged in as {0.user}'.format(client))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  print(response)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
'''
#========================================
#AUDIO PLAYER BEGINS HERE
#========================================

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
  'format': 'bestaudio/best',
  'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostderr': False,
  'quiet': True,
  'no_warnings': True,
  'default_search': 'auto',
  'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
  'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
  def __init__(self, source, *, data, volume=0.5):
    super().__init__(source, volume)
    self.data = data
    self.title = data.get('title')
    self.url = data.get('url')
  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
    loop = loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=notstream))
    if 'entries' in data:
      # take first item from a playlist
      data = data['entries'][0]
    filename = data['url'] if stream else ytdl.prepare_filename(data)
    return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def join(self, ctx, *, channel: discord.VoiceChannel):
    """Joins a voice channel"""
    if ctx.voice_client is not None:
      return await ctx.voice_client.move_to(channel)
    await channel.connect()
  @commands.command()
  async def play(self, ctx, *, query):
    """Plays a file from the local filesystem"""
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
    ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('Now playing: {}'.format(query))

  @commands.command()
  async def yt(self, ctx, *, url):
    """Plays from a url (almost anything youtube_dl supports)"""

    async with ctx.typing():
      player = await YTDLSource.from_url(url, loop=self.bot.loop)
      ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(player.title))

  @commands.command()
  async def stream(self, ctx, *, url):
    """Streams from a url (same as yt, but doesn't predownload)"""

    async with ctx.typing():
      player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
      ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('Now playing: {}'.format(player.title))

  @commands.command()
  async def volume(self, ctx, volume: int):
    """Changes the player's volume"""

    if ctx.voice_client is None:
      return await ctx.send("Not connected to a voice channel.")

    ctx.voice_client.source.volume = volume / 100
    await ctx.send("Changed volume to {}%".format(volume))

  @commands.command()
  async def stop(self, ctx):
    """Stops and disconnects the bot from voice"""

    await ctx.voice_client.disconnect()

  @play.before_invoke
  @yt.before_invoke
  @stream.before_invoke
  async def ensure_voice(self, ctx):
    if ctx.voice_client is None:
      if ctx.author.voice:
        await ctx.author.voice.channel.connect()
      else:
        await ctx.send("You are not connected to a voice channel.")
        raise commands.CommandError("Author not connected to a voice channel.")
    elif ctx.voice_client.is_playing():
      ctx.voice_client.stop()
'''

#========================================
#AUDIO PLAYER END HERE
#========================================


@client.event
async def on_message(message):
  guild = client.get_guild(707159521457340466) 
  if message.author == client.user:
    return

  if "oss" == message.content.lower():
    dialogsArray = [
    ["J\'aime me beurrer la biscotte!"],
    ["**Hubert** : J’ai été réveillé par un homme qui hurlait à la mort du haut de cette tour ! J’ai dû lefaire taire.",
    "**Larmina** : Quoi ?! Vous avez fait taire le muezzin !!",
    "**Hubert** : Ah ! C’était donc ça tout ce tintouin."],
    [" Mais ce sera surtout l’occasion de rencontrer le gratin cairote. Et non pas le gratin de pommes deterre !"],
    ["C’est marrant, c’est toujours les nazis qui ont le mauvais rôle. Nous sommes en 1955, Herr Bramard, onpeut avoir     unedeuxième chance, merci."],
    ["Tu n’es pas seulement un lâche, tu es un traître, comme ta petite taille le laissait deviner."],
    ["En tout cas, on peut dire que le soviet éponge..."],
    ["J’aime quand on m’enduit d’huile..."],
    ["Vous savez déjà ce que ça fait un million, Larmina ?"],
    ["C’est notre RAIS a nous, René Coti ! Un grand homme, il marquera l’histoire, il aime les Cochinchinois,les Malgaches     les Sénégalais, les Marocains... C’est donc ton ami."],
    ["Nous avons besoin de vous sur place. Un expert. Un spécialiste du monde arabo-musulman..."],
    [" Vous avez bien une amicale des anciens nazis ? un club ? une association peut-être ?"],
    ["**Hubert** : Voilà, cadeau... de Noël !",
    "**Dolorès** : Merci.",
    "**Hubert** : Non, je dis cadeau de Noël, parce que c’est par rapport à mon prénom",
    "**Dolorès** : Oui, c’est ce que j’avais compris.",
    "**Hubert** : Sinon y’a,... y’a aussi les boules...",
    "**Dolorès** : De Noël...?",
    "**Hubert** : Oui !! ... Ohhh, oh si c’est rigolo !"],
    ["**Dolorès** : Et comment vous appelez un pays qui a comme président un militaire avec les pleinspouvoirs, une police     secrète, une seule chaîne de télévision et dont toute l’information est contrôléepar l’État ?",
    "**Hubert** : J’appelle ça la France mademoiselle, et pas n’importe laquelle, la France du général DeGaulle."],
    ["**Hubert** : Rechercher un nazi avec des juifs... Quelle drôle d’idée !",
    "**Dolorès** : Et pourquoi donc ?",
    "**Hubert** : Mais enfin, il va les reconnaître.",
    "**Dolorès** : Comment ça ?",
    "**Hubert** : Bah je sais pas le nez déjà, les oreilles, les yeux..."]
    ]
    # randint generates a random integar between the first parameter and the second
    randomDialog = random.randint(0, len(dialogsArray)-1)
    dialogArray = dialogsArray[randomDialog]
    for dialogLine in dialogArray:
      await message.channel.send(dialogLine)
      print(dialogLine)
  elif "quote" == message.content.lower():
    quote = get_quote()
    await message.channel.send(quote)
  elif "vous savez quoi" == message.content.lower():
    await message.channel.send("Vous savez, moi je ne crois pas qu'il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd'hui avec vous, je dirais que c'est d'abord des rencontres. Des gens qui m'ont tendu la main, peut-être à un moment où je ne pouvais pas, où j'étais seul chez moi. Et c'est assez curieux de se dire que les hasards, les rencontres forgent une destinée... Parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l'interlocuteur en face je dirais, le miroir qui vous aide à avancer. Alors ça n'est pas mon cas, comme je disais là, puisque moi au contraire, j'ai pu : et je dis merci à la vie, je lui dis merci, je chante la vie, je danse la vie... je ne suis qu'amour ! Et finalement, quand beaucoup de gens aujourd'hui me disent « Mais comment fais-tu pour avoir cette humanité ? », et bien je leur réponds très simplement, je leur dis que c'est ce goût de l'amour ce goût donc qui m'a poussé aujourd'hui à entreprendre une construction mécanique, mais demain qui sait ? Peut-être simplement à me mettre au service de la communauté, à faire le don, le don de soi...")
  elif "kamoulox" == message.content.lower():
    phraseTotal = ""
    kamouloxPhrases = [
      ["Je bois", 
      "et je nettoie"],
      ["Je photocopie",
      "et j'achète"],
      ["Je démonte",
      "et j'envoie un fax à"],
      ["Je saute sur",
      "et je respire"],
      ["Ah non impossible il y a",
      "qui repeint",
      "en diagonale"],
      ["Vous êtes marié ? Non, je conduis avec"],
      ["Je crache sur", "et je viole"],
      ["Je mange", "et je roule"],
      ["Je barbouille", "et je ressemble à"],
      ["J'invente", "à voile et je déclare la guerre à"],
      ["Vous ne pouvez pas, il y a",
      "qui se rase",
      "en opposition"],
      ["J'invite",
      "et je doigte"],
      ["Je me met la main dans", "et je cours derrière"],
      ["Je badigeonne", "d'huile solaire, et je compte jusqu'à"],
      ["Je tente", "manouche"],
      ["Je mets", "et j'apprends le kung fu à "],
      ["Je rabote", "et je tête"],
      ["J'amadoue", "et je jette Mamie dans les orties en case", "moldave"],
      ["Je déguise", "et je me marie avec"],
      ["Je caresse", "et je pue du"],
      ["Je m'introduis chez Dark Vador et je mets", "dans son casque"],
      ["Je mange", "et je tutoie"],
      ["Eh non, Casimir joue aux fléchettes avec une poule en case moule soviet"],
      ["","ou","? Je prends la"],
      ["Vous tentez", "malgache"]
    ]
    # randint generates a random integar between the first parameter and the second
    randomKamoulox = random.randint(0, len(kamouloxPhrases)-1)
    kamouloxArray = kamouloxPhrases[randomKamoulox]
    for kamouloxLine in kamouloxArray:
      kamouloxMots = [
        "une orange",
        "une pomme de terre",
        "une pomme",
        "une tomate",
        "un oignon",
        "une salade",
        "une courgette",
        "un poireau",
        "un lave linge",
        "Christophe Maé",
        "Christophe Willem",
        "Michael Jackson",
        "Mel Gibson",
        "Jacques Chirac",
        "François Mitterrand",
        "une poule",
        "une vache",
        "un porc",
        "un sanglier",
        "Georges Pompidou",
        "Valéry Giscard d'Estaing",
        "François Hollande",
        "Nicolas Sarkozy",
        "Charles de Gaulle",
        "Colonel Moutarde",
        "chandelier",
        "SIA",
        "Lady Gaga",
        "la reine d'angleterre",
        "Stéphanie de Monaco",
        "les Spice Girls",
        "ABBA",
        "Boney M",
        "Whoopi Goldberg",
        "une cuillère",
        "une chèvre",
        "une montagne",
      ]
      randomMots = random.randint(0, len(kamouloxMots)-1)
      MotsArray = kamouloxMots[randomMots]
      phraseTotal+=kamouloxLine+ " " +MotsArray+ " "
    await message.channel.send(phraseTotal)

@tasks.loop(seconds=60)
async def change_status():
  statusDialog = [
    "J\'aime me beurrer la biscotte!",
    " Mais ce sera surtout l’occasion de rencontrer le gratin cairote. Et non pas le gratin de pommes deterre !",
    "Tu n’es pas seulement un lâche, tu es un traître, comme ta petite taille le laissait deviner.",
    "En tout cas, on peut dire que le soviet éponge...",
    "J’aime quand on m’enduit d’huile...",
    "Vous savez déjà ce que ça fait un million, Larmina ?",
    "C’est notre RAIS a nous, René Coti ! Un grand homme, il marquera l’histoire, il aime les Cochinchinois,les Malgaches     les Sénégalais, les Marocains... C’est donc ton ami.",
    "Nous avons besoin de vous sur place. Un expert. Un spécialiste du monde arabo-musulman...",
    " Vous avez bien une amicale des anciens nazis ? un club ? une association peut-être ?",
    ]
  await client.change_presence(activity=discord.Game(choice(statusDialog)))

keep_alive()
client.run(os.getenv("TOKEN"))
#bot.add_cog(Music(bot))
#bot.run(os.getenv("TOKEN"))