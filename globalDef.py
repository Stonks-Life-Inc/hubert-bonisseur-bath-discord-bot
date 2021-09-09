from array import *
import random 
from random import choice 
import requests

# Purpose: pick a random string from an array
def customFromString(customString):
  randomDialog = random.randint(0, len(customString)-1)
  dialogArray = customString[randomDialog]
  return dialogArray

# Simple commande texte "Quote"
# Affiche une citation aléatoire en utilisant l'API https://zenquotes.io/api/random    
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  print(response)
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)