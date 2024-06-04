#RPG classes, Yazan Saleh
#May 29th, 2024

#This code is for classes in my TBRPG


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
            'A literal piece of laser, I dont know how one would wield it however..',
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

#List of of the woods
wood =[['Tree', 'Empty', 'Tree', 'Empty', 'Suspicious Tree', 'Empty'],
            ['Empty', 'Empty', 'Empty', 'Path', 'Path', 'Path'],
            ['Empty', 'Path', 'Path', 'Empty', 'Empty', 'Empty'],
            ['Tree', 'Bush', 'Empty', 'Empty', 'Tree', 'Empty']]

#List of of the river
riv = [['Water', 'Water', 'Pier', 'Boat', 'Empty', 'Water'],
         ['River', 'River', 'River', 'River', 'River', 'River'],
         ['Upstream', 'Riverbank', 'Riverbank', 'Riverbank', 'River', 'Downstream'],
         ['Empty', 'Empty', 'Path', 'Empty', 'Tree', 'Empty']]

#List of of the mounatins
mount = [['Sun', 'Empty', 'Empty', 'Empty', 'Mountainside', 'Path'],
               ['Empty', 'Empty', 'Mountain', 'Empty', 'Empty', 'Empty'],
               ['Empty', 'Mountainside', 'Branch', 'Mountain', 'Empty', 'Empty'],
               ['Still the', 'mountain', 'Empty', 'Cave entrance', 'Empty', 'Empty']]

#List of of the abandoned village
vil = [['Empty well', 'Empty', 'Empty', 'Empty', 'Empty', 'Empty'],
         ['Empty', 'House', 'Road', 'Empty', 'Overgrown Fence', 'Empty'],
         ['Closed Streetlamp', 'Empty', 'Road', 'Empty', 'House', 'Empty'],
         ['Empty', 'Empty', 'Empty', 'Road', 'Empty', 'Empty']]

class Inv:
    def __init__(self, choice):
        self.choice = choice.lower().strip()
        self.weapon = inventory['weapons']
        self.potion = inventory['potions']
        self.rune = inventory['runes']
        
    def use(self):
        pass
        
class Weapon(Inv):
    def __init__(self, choice):
        super().__init__(choice)
    
    def show_weapon(self):
        if self.choice in self.weapon:
            print(f"{self.choice.title()}:")
            for desc, info in self.weapon[self.choice].items():
                print(f"{desc.title()}: {info}")
        else:
            print("That's not a weapon that we have")
                
class Potions(Inv):
    def __init__(self, choice):
        super().__init__(choice)
        
    def show_potion(self):
        if self.choice in self.potion:
            print(f"{self.choice.title()}: {self.potion[self.choice]}")
        else:
            print("Thats not a potion we have")
            
class Runes(Inv):
    def __init__(self, choice):
        super().__init__(choice)
        
    def show_rune(self):
        if self.choice in self.rune:
            print(f"{self.choice.title()}: {self.rune[self.choice]}")
        else:
            print("We dont have that")
                
def simple(var):
    print(var)

class Map:
    def __init__(self, place):
        self.place = place
        if self.place == wood:
            self.current_position = [2, 0]
        elif self.place == riv:
            self.current_position = [3, 3]
        elif self.place == mount:
            self.current_position = [0, 2]
        elif self.place == vil:
            self.current_position = [2, 5]
        self.action = ''

    def move(self, direction):
        x, y = self.current_position
        max_x = len(self.place) - 1
        max_y = len(self.place[0]) - 1



        if direction == 'right' and y < max_y:
            y += 1
        elif direction == 'left' and y > 0:
            y -= 1
        elif direction == 'up' and x > 0:
            x -= 1
        elif direction == 'down' and x < max_x:
            x += 1
        else:
            print("You can't go that way!")
            return

        self.current_position = [x, y]
        if self.place[x][y] == 'River':
            print("you can't cross this")
            x += 1
        elif self.place[x][y] == 'Downstream':
            answer = input("Do you want to continue downstream?")
            if answer.lower() == 'yes':
                print("That's all")
                quit()
            else:
                return
        elif self.place[x][y] == 'Upstream':
            answer = input("Do you want to continue upstream?")
            if answer.lower() == 'yes':
                print("That's all")
                quit()
            else:
                return

        if self.place[x][y] == 'Suspicious Tree':
            answer = input("Do you want to enter the suspicious tree?")
            if answer.lower() == 'yes':
                print("That's all")
                quit()
            else:
                return
            
        if self.place[x][y] == 'Cave entrance':
            answer = input("Do you want to enter the cave?")
            if answer.lower() == 'yes':
                print("That's all")
                quit()
            else:
                return
        
        if self.place[x][y] == 'House':
            answer = input("Do you want to enter the house?")
            if answer.lower() == 'yes':
                print("That's all")
                quit()
            else:
                return

        if self.place[x][y] == 'Empty':
            print('You can check your inventory or continue')
            self.action = input("What would you like to do?").lower()
            actions = ['continue', 'inventory']
            while self.action in actions:
                if self.action == 'continue':
                    return self.action
                elif self.action == 'inventory':
                    return self.action
                else:
                    print("That isn't an option")

        self.current_position = [x, y]    
        print(f"You moved {direction}. You are now at position {self.current_position}. The place is {self.place[x][y]}")

        
        



