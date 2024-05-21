#RPG Modules And Maps, Yazan Saleh
#This code will create a map for my TBG RPG Mysteries of Wynn

#There are lines of code which are purely for space 
#and for waiting before continuing the rest of the program


#Imports
from random import randint
import time
import MoW_Modules as md

# The initial Text
text = '███    ███ ██    ██ ███████ ████████ ███████ ██████  ██ ███████ ███████ .\
████  ████  ██  ██  ██         ██    ██      ██   ██ ██ ██      ██      .\
██ ████ ██   ████   ███████    ██    █████   ██████  ██ █████   ███████ .\
██  ██  ██    ██         ██    ██    ██      ██   ██ ██ ██           ██ .\
██      ██    ██    ███████    ██    ███████ ██   ██ ██ ███████ ███████ .\
                                                                        .\
                                                                        .\
 ██████  ███████                                                        .\
██    ██ ██                                                             .\
██    ██ █████                                                          .\
██    ██ ██                                                             .\
 ██████  ██                                                             .\
                                                                        .\
                                                                        .\
██     ██ ██    ██ ███    ██ ███    ██                                  .\
██     ██  ██  ██  ████   ██ ████   ██                                  .\
██  █  ██   ████   ██ ██  ██ ██ ██  ██                                  .\
██ ███ ██    ██    ██  ██ ██ ██  ██ ██                                  .\
 ███ ███     ██    ██   ████ ██   ████'

#Splits the text into parts and displays it one line at a time
new= text.split(".")
list(map(md.simple, new))

#Waits a little bit
wait = time.sleep(0.5)
wait

#This displays the initail choices
first_choices = ['\n*quit', '\n*characters', '\n*map']
player_char = ''
player_loc = ''

#This loop keeps running as long as there are at least 2 options available
while len(first_choices) > 1 :
    print()
    #If map was chosen first
    if '\n*map' not in first_choices:
        print("We'll need to pick a character before we venture any further!\n")
    
    #Prompts the player for their next action
    answer = input(f"What do you want to do? (choose from below) \
    {''.join(first_choices)}\nAction: ")

    #Makes sure that the answer is lowercase with no spaces
    answer = answer.lower()
    answer = answer.strip()
    
    if answer == 'quit':
        quit #Quits if quit is chosen
    
    elif answer == 'characters' or answer == 'character' or answer == 'char':
        first_choices.remove('\n*characters')
        print("\nThe characters are:")
        for c,d in md.character():#loops thorugh the character options
            time.sleep(0.4)
            print(c.title())

        char_choices = ['warrior', 'mage']
        while player_char not in char_choices:
            #Prompts the player for which character they want
            char_choice = input("\nWhich one do you want to choose?\n")
            char_choice = char_choice.lower()
            char_choice = char_choice.strip()
            
            if char_choice == 'warrior':
                print()
                player_char = 'warrior'
                #Loops through the warrior's characteristics 
                for attribute, stat in md.play('warrior').items():
                    print(f"{attribute.title()}: {stat}")
                    time.sleep(0.3)
                print()

            elif char_choice == 'mage':
                print()
                player_char = 'mage'
                #Loops through the mage's characteristics 
                for attribute, stat in md.play('mage').items():
                    print(f"{attribute.title()}: {stat}")
                    time.sleep(0.2)
                print()

            else:#Ensure that only mage or warrior ae selected
                print('Only the Warrior or the Mage are worthy')
    
    elif answer == 'map':
        first_choices.remove('\n*map')
        print()
        possible_player_locations = ['woods', 'river', 'mountains', 'village']
        while player_loc not in possible_player_locations:
            for place, desc in md.places():#Iterates through the places
                time.sleep(0.4)
                print(f"{place.title()}: {desc}")
                
            #Prompts the player for where they want to go
            chosen_l = input("\nWhere do you want to go?\n")
            chosen_l = chosen_l.lower()
            chosen_l = chosen_l.strip()
            print()
            
            if chosen_l == 'woods' or 'east':
                md.woods()#Prints the woods ASCII art
                player_loc = 'woods'
                
            elif chosen_l == 'mountains' or 'west':
                md.mountains()#Prints the mountain ASCII art
                player_loc = 'mountains'
                
            elif chosen_l == 'river' or 'north':
                md.river()#Prints the river ASCII art
                player_loc = 'river'
                
            elif chosen_l == 'village' or 'south' or 'abandoned village':
                md.village()#Prints the village ASCII art
                player_loc = 'village'
                
            else:#Ensures that only the listed lications are chosen
                print(f"Just one of the locations or directions.")
    
    else:#Ensures that only the listed choices are chosen
        print(f"\nJust one of the {len(first_choices)} options.")


time.sleep(0.3)
print("\nLet's see your inventory and describe your surroundings now: ")

#Places the chosen location and character in a list
place_char = [player_loc, player_char]

possible_weapons = ['sword', 'gun', 'grimoire', 'flail', 'laser']
possible_potions = ['void', 'foreshadowing', 'unbreaking',  'healing']

new_weapon = ''
new_potion = possible_potions[randint(0,3)]


#Shows more descriptions of each location
#Depending on what's chosen
if place_char[0] == 'woods':
    print("You find a deep, dark woods\n\
that you can't see very deep into,\n\
you just know that there are no dangerous creatures ahead.")
    
elif place_char[0] == 'mountains':
    print("You are at the base of a great mountain range\n\
you see the entrance of a cave to your left,\n\
a path around the mountain to your right\n\
and a slow incline in front of you...")
    
elif place_char[0] == 'river':
    print("You are next to a riverbank, you look to your left\n\
and you see the river climbing upwards out of your sight\n\
and to your right, you see the river stretching out to the horizon.")
    
elif place_char[0] == 'village':
    print("You find yourself in an abandoned village,\n\
(at least, you think so...)")

time.sleep(3)

#Gives the player a random weapon depending on the choice
if place_char[1] == 'warrior':
    warrior_weapons = ['sword', 'gun', 'flail']
    new_weapon = warrior_weapons[randint(0,2)]
    md.weapons(new_weapon)
elif place_char[1] == 'mage':
    mage_weapons = ['grimoire', 'gun', 'laser']
    new_weapon = mage_weapons[randint(0,2)]
    md.weapons(new_weapon)

time.sleep(2)
#Gives the player a random potion
md.potions(new_potion)