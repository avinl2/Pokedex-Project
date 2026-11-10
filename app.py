import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
moves = open("./moves.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
collection = json.load(moves)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

#x=0
#for x in range(809):
   #x<809
   #print(data[x]["name"])

# Add a language choice feature and print the pokemons name based on the user input

#def characters(language):
   #for x in range(809):
      #print(data[x]["name"][language])
#language = input("What language do you want?")
#characters(language)

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type information.

language = input("What language do you want?")
def search(pokemon_type):
   for pokemon in data:
      if pokemon_type in pokemon["type"]:
         print(pokemon["name"][language])
pokemon_type = input("What pokemon type do you want?")
search(pokemon_type)

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
while True:
   def find(pokemon_name):
      total=0
      for pokemon in data:
         if pokemon_name in pokemon["name"][language].lower():
            print(pokemon["name"][language])
         elif pokemon_name not in pokemon["name"][language].lower():
            total+=1
      if total == 809:
         print("There is no pokemon with that name.")
         total=0
   pokemon_name = input("What pokemon are you trying to find?")
   find(pokemon_name)
# find a way to break the loop

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
