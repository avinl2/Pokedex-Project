import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
#x=0
#for x in range(809):
   #x<809
   #print(data[x]["name"])
# Add a language choice feature and print the pokemons name based on the user input
def characters(language):
   for x in range(809):
      print(data[x]["name"][language])
language = input("What language do you want. (french, english, japanese, or chinese)")
characters(language)
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user.
language = input("What language do you want?")
def search(pokemon_type):
   for pokemon in data:
      if pokemon_type in pokemon["type"]:
         print(pokemon["name"][language])
pokemon_type = input("What pokemon type do you want?")
search(pokemon_type)
# Develop a function to
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

