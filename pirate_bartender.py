"""This pirate bartender program will ask you for drink
preferences and create a drink for you."""

import random
import sys


questions = {
  "strong": "Do ye like yer drinks strong?",
  "salty": "Do you like it with a salty tang?",
  "bitter": "Are ye a lubber who likes it bitter?",
  "sweet": "Would ye like a bit of sweetness with yer poison?",
  "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
  "strong": ["glug of rum", "slug of whisky", "splash of gin"],
  "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
  "bitter": ["shake of bitters", "splash of tonic", "twist of lemon"],
  "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
  "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ['Salty ', 'Killer ', 'Woozy ', 'Slimy ', 'Feisty ']
nouns = ["Parrot", "Peg Leg", "Crossbones", "Treasure", "Galleon"]

stock = {
  "glug of rum": 2,
  "slug of whisky": 1,
  "splash of gin": 5,
  "olive on a stick": 4,
  "salt-dusted rim": 3,
  "rasher of bacon": 7,
  "shake of bitters": 3,
  "splash of tonic": 3,
  "twist of lemon": 2,
  "sugar cube": 1,
  "spoonful of honey": 5,
  "splash of cola": 4,
  "slice of orange": 2,
  "dash of cassis": 2,
  "cherry on top": 1,
}



customers = {}

def get_name():
  """Gets customer name.  Also allows quit out of program."""
  customer_name = raw_input("What's yer name, pal?  (Q to quit) ")
  if customer_name.lower() == 'q':
    sys.exit(0)
  return customer_name
  
def ask_questions():
  answers = {}  
  """Asks 5 questions about drink preference and returns a dict with booleans."""
  for question in questions:
    answers[question] = raw_input("{} [y/n]: ".format(questions[question]))
    
  for answer in answers:
    if answers[answer].lower() in ("yes", "y"):
      answers[answer] = True
    else:
      answers[answer] = False
  return answers

def name_drink():
  """Names drink with random choices from lists."""
  return random.choice(adjectives) + random.choice(nouns)

def decrease_stock(drink):
  """Decreases ingredient stock."""
  for ingredient in drink:
    supply[ingredient] -= 1
    
def check_stock():
  """Checks ingredient stock and restocks if zero."""
  for item in supply:
    if supply[item] == 0:
      print "We need more {}.  I'll send the parrot over to the store to get some.\n".format(item)
      supply[item] = 10

def make_drink(drink_preference):
  """Makes drink based on drink preferences of customer."""
  drink = []
  drink_name = name_drink()
  for preference in drink_preference:
    if drink_preference[preference] == True:
      drink.append(random.choice(ingredients[preference]))
  print "\nI think you'll like the {}.\n\nThe ingredients are: ".format(drink_name)
  for ingredient in drink:
    print ingredient
  print "\nEnjoy!\n"
  decrease_stock(drink)
  check_stock()
  return drink



if __name__ == "__main__":
  while True:
    name = get_name()
    if name not in customers:
      preferences = ask_questions()
      customers[name] = preferences
    else:
      preferences = customers[name]
    while True:
      make_drink(preferences)
      new_drink = raw_input("Would you like another drink? (y/n): ")
      if new_drink.lower() not in ("y", "yes"):
        break
      


                                  
                                  
                                  
                                  
                                  
                                 
                                  
                                  