#RPG Modules And Maps, Yazan Saleh
#This code contains dictionaries and functions to import
#Into the main code and use
import time

#Characters nested dictionary
player = {
    'warrior' : {
        'name' : 'Stone',
        'health' : 100,
        'defense' : 10,
        'dexterity' : 20,        
        'strengths' : 'brave, skilled and strong',
        'weaknesses' : 'cautious and scared of water',
        },
    'mage' : {
        'name' : 'Skip',
        'health' : 50,
        'defense' : 5,
        'dexterity' : 80,
        'strengths' : 'quick, sharp and accurate',
        'weaknesses' : 'distracted and frail',
        }
    }

#Loactions dictionary
locations = {
    'river' : 'A seemingly endless river stretching out far past the horizon. (North)',
    'mountains' : 'A tall foreboding mountain that hides secrets within it. (West)',
    'abandoned village' : 'A village that seems well-maintained, despite being abandoned. (South)',
    'woods' : 'A forest which has a magical aura around it. (East)'
    }

#Inventory items nested dictionary
inventory = {
    'weapons' : {
        'sword' : {
            'description' :
            'A boradswrord that seems to always be sharp.',
            'damage' : '20-40',
            'range' : 10
            },
        'gun' : {
            'description' :
            'A basic revolver that automatically reloads',
            'damage' : '50-80',
            'range' : 'Depending on accuracy'
            },
        'grimoire' : {
            'description' :
            'A spellbook whose words become clearer as you learn',
            'damage' : '80-90',
            'range' : 'Depending on mana'
            },
        'flail' : {
            'description' :
            'A medival weapon that hits like a rock but is light as a feather to the user',
            'damage' : '30-50',
            'range' : 30
            },
        'laser' : {
            'description' :
            'A literal pice of laser, I dont know how one would wield it however..',
            'damage' : 50,
            'range' : "infinite, just don't miss.."
            }
        },
    'potions' : {
        'foreshadowing' :
        'allows you to temporarily see a few seconds into the future',
        'void' : 'allows you to create a storage void',
        'unbreaking' : 'grants invincibility for 5 seconds',
        'healing' : 'heals when applied'
        },
    'runes' : {
        'reflection' : 'reflects some damage dealt',
        'defense' : 'strengthens and reinforces',
        'invisibility' : "hides what it's attatched to",
        'substitution' : 'switches with an object when user is in fatal danger'
        }
    }

#ASCII art of the woods
wood = '+-------------+---------------+---------------+---------------+---------------+---------------+.\
|    Tree     |               |     Tree      |               |Suspicious Tree|               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|             |               |               |     Path      |      Path     |     Path      |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|     You     |     Path      |     Path      |               |               |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|    Tree     |     Bush      |               |               |     Tree      |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+'
     
#ASCII art of the river
riv = '+-------------+---------------+---------------+---------------+---------------+---------------+.\
|    Water    |     Water     |      Pier     |     Boat      |     Tree      |    Water      |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|    River      |    River      |    River      |    River      |    River      |    River      |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|   Upstream  |   Riverbank   |    Riverbank  |   Riverbank   |               |   Downstream  |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|             |               |      Path     |     You       |     Tree      |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+'
    
#ASCII art of the mounatins
mount ='+-------------+---------------+---------------+---------------+---------------+---------------+.\
| Sun         |               |               |               |   Mountainside|Path           |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|             |               |   Mountain    |               |     Tree      |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|             |  Mountainside |Branch         |  Mountain     |               |      You      |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|    Still the|mountain       |               |  Cave entrance|               |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+'

#ASCII art of the abandoned village
vil = '+-------------+---------------+---------------+---------------+---------------+---------------+.\
|        Empty|Well           |      You      |               |               |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|             |    House      |    Road       |               |      Overgrown|fence          |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|       Closed|Streetlamp     |      Road     |               |     House     |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+.\
|             |               |               | Road          |               |               |.\
+-------------+---------------+---------------+---------------+---------------+---------------+'
    

#A simple loop with a short delay
def simple(var):
    print(var)
    time.sleep(0.1)#0.1

#A function that maps the ASCII art of the village
def village():
    new = vil.split('.')
    list(map(simple, new))

#A function that maps the ASCII art of the woods    
def woods():
    new = wood.split('.')
    list(map(simple, new))

#A function that maps the ASCII art of the mountains
def mountains():
    new = mount.split('.')
    list(map(simple, new))

#A function that maps the ASCII art of the river         
def river():
    new = riv.split('.')
    list(map(simple, new))

#A function which returns the keys of the player dictionary   
def character():
    return player.items()

#A function which returns the attributes of the chosen character
def play(choice):
    return player[choice]

#A function which returns the keys of the location dictionary
def places():
    return locations.items()

#A function which iterates the attributes depending on the chosen weapon
def weapons(choice):
    print(f"\nYour weapon is a {choice.title()}: ")
    for weapon, parts in inventory['weapons'][choice].items():
        print(f"  {weapon.title()}: {parts}")

#A function which iterates through the chosen potion and its description
def potions(choice):
    print(f"\nYou also have a {choice.title()} potion:")
    print(f"  {inventory['potions'][choice].title()}")