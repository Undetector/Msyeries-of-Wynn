#MoW with continuous Gameplay, Yazan Saleh
#This code will be for my TBRPG, Mysteries of Wynn

#The game will be a continuous Text Based Game which will have at least 20
#Decisions that the player will be able to act upon

import time
import sys

#The text that I will use for the intro, ending and death
intro = "\nWelcome to the..."
intro2 = '\n███    ███ ██    ██ ███████ ████████ ███████ ██████  ██ ███████ ███████ |\
████  ████  ██  ██  ██         ██    ██      ██   ██ ██ ██      ██      |\
██ ████ ██   ████   ███████    ██    █████   ██████  ██ █████   ███████ |\
██  ██  ██    ██         ██    ██    ██      ██   ██ ██ ██           ██ |\
██      ██    ██    ███████    ██    ███████ ██   ██ ██ ███████ ███████ |\
                                                                        |\
                                                                        |\
 ██████  ███████                                                        |\
██    ██ ██                                                             |\
██    ██ █████                                                          |\
██    ██ ██                                                             |\
 ██████  ██                                                             |\
                                                                        |\
                                                                        |\
██     ██ ██    ██ ███    ██ ███    ██                                  |\
██     ██  ██  ██  ████   ██ ████   ██                                  |\
██  █  ██   ████   ██ ██  ██ ██ ██  ██                                  |\
██ ███ ██    ██    ██  ██ ██ ██  ██ ██                                  |\
 ███ ███     ██    ██   ████ ██   ████'
intro3 = "\nWhat will you find?"
ending = "\nCongratulations! You have discovered the Mysteries of Wynn\
 and must keep it all safe from the public"
die = "\nOh no you died... Do you want to restart?"

#These are functions for those pieces of text
def prints_t(text, speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(speed)
def prints(text, leng):
    new= text.split("|")
    for i in new:
        print(i)
        time.sleep(leng)
def start():
    prints_t(intro, 0.1)
    prints(intro2, 0.1)
    prints_t(intro3, 0.1)
    time.sleep(0.2)
def end():
    prints_t(ending, 0.1)
def death():
    prints_t(die, 0.1)
    #Asks the player if they want to restart after they die
    decision_d_5 = input('\nDo you want to restart? '
                            '(yes, no) ').lower().strip()

    #Keeps asking the player until they input a valid answer
    while decision_d_5 not in ('yes', 'no'):
        print("Just one of the options: yes or no")
        decision_d_5 = input('\nDo you want to restart? '
                                '(yes, no) ').lower().strip()

    if decision_d_5 == 'yes':
        main()
    elif decision_d_5 == 'no':
        print('ok.')
        time.sleep(1)
        quit()

#This controls the speed of most of the text
speed = 0.01
   
#These are lists and inventories that I will add to throughout the game
inventory = {}
choices = []
group = []

#These are functions that show off the story before each subsequnet choice
#This is the function that plays the initial text
def choice1():
    starting = '''
\nYou are a man living a crazy and exciting life in medieval-ish times, 
being a vigilante that steals from corrupt officials and gives the money to people who deserve it, 
both rich and poor. One day, you happen upon a scroll, 
you gave it to your childhood friend who also happens to be a librarian, 
Skipp (He always preferred the double P) but curiosity gets the better of you, 
so you open up the scroll and find a map that seems to lead to a place called "Wynn", 
you knew nothing about it so you ask your friend what it was about. 
He drops whatever he was doing and runs up to you, exclaiming, "Do you have any idea what this means??", 
you shake your head no but ask if you should be excited. 
Skipp ignores your question and asks a question of his own,
'''
    prints_t(starting, speed)

#This one is after you agree to the adventure
def choice2():
    prints_t('\nSkipp excitedly tells you to pack up your stuff and meet him '
             'in front of the library tomorrow morning.', speed)
    prints_t('\nIn the morning, you get your sword, put a dagger in you boot, '
             'get a few potions, hide a few runes around your clothing and bring some food in a backpack. '
             'When you get back to the library, you see Skipp hauling a huge bag filled to the brim '
             'with provisions,and miscellaneous things that look heavy, you ask him if everything '
             'he brought is necessary,he responds with, "I mean...we ARE gonna be gone a while, '
             'I think we gotta have all of these...right?" ', speed)

#This one is when Skye confronts you both
def choice3():
    prints_t('\nYou both embark on your adventure, heading towards the Kigler mountains '
             'which are known for their dangerous chasms, monsters and traps, but everyone '
             'knew that there was a great treasure hidden deep within, if you survived...', speed)
    prints_t('\nOn your way, right outside the walls of the kingdom of Runder, you both are '
             'startled by a loud voice that seemed to be coming from behind you, yelling, '
             '''"Where do YOU TWO think you're going off to??" when you turn around, '''
             '''you are greeted by yours and Skipp's childhood best friend, Skye, a mercenary '''
             '''and a loudmouth, who's helped you with your work from time to time. '''
             'Skipp meekly replies, "..to..uhh...to solve the treasure of Wynn..." '
             '''Skye: "I know! I overheard you guys earlier! I'm mad you guys didn't invite me! '''
             'You know how much I love ADVENTURE!" You defeatedly agree to let her travel with '
             "you, but before doing so, you tell her to get some stuff, she tells you she's "
             'already ready and pull out a large bag with enough provisions for a month.', speed)
    prints_t('\nBefore going off too far, you spot a glowing ring behind a tree, '
             'do you take it with you?', speed)

#This one is when you get the feeling of someone watching
def choice4():
    prints_t("\nWhile discussing code words that you will use when in trouble, "
             "you approach the woods on your way to the mountains, you feel like there's "
             "someone...or something watching you.", speed)

#These are the choices for when you trust your gut feeling
def choice5():
    prints_t('\nYou spot a suspicious Tree and Rock near your party', speed)

#This one is for when you choose the suspicious tree
def choice6():
    prints_t("\nYou find and hold down an archer who immediately whistles out loud, "
             "alerting an assassin who jumps up from behind a rock and tries to attack you. "
             "What do you do?", speed)

#This one asks you what you do right before the arrow is shot
def choice7():
    prints_t("\nJust as Sky tackles the assassin, they yell out some sort of signal "
             "which prompts you to quickly scan the area, you see the glint of an arrow "
             "right before it was shot, you yell to warn Skye but she’s too slow to react "
             "What do you do?", speed)

#This one prompts you with either handing over the provisions or to use the code word
def choice8():
    prints_t("\nYou turn around to confront the assassin but that allows "
             "the archer to free themself and take you hostage, they hold "
             "you by the neck and demanded that your party drop their "
             "weapons and provisions.", speed)
    
#8  #Adds to the choices list
    choices.extend(('hand over', 'code word'))
    decision_8 = input("Do you hand over your provisions or do you try your unrehearsed code word?" 
                        "(hand over, code word) ").lower().strip()
    while decision_8 not in choices:
        print('Just one of the options')
        decision_8 = input("Do you hand over your provisions or do you try your unrehearsed code word?" 
                           "(hand over, code word) ").lower().strip()

    if decision_8 == 'hand over':
        prints_t("Your team defeatedly hands over the provisions", speed)
        inventory.pop('provisions')
        inventory.pop('Sword')
        inventory.pop('Potions')
    elif decision_8 == 'code word':
        prints_t('\nYou yell out the code word, "Arkud!" but it just confuses everyone in your team '
                 'but prompts the enemies to kill you immediately ', speed)
        death()
    choices.clear()

    choice10()

#This one prompts you for whether you show Skye that you trust the enemies or not
def choice9():
    prints_t("\nYou run in and jump in between the arrow and Skye, it gets you "
             "in the leg and you feel your body go into agonizing pain "
             "Skipp puts up a light barrier around the archer before trapping "
             "him with the binding spell.", speed)
    prints_t("/nYou feel the poison coursing through your body "
             "The assassin tells you that they can help you, but only if you help them "
             "Skye asks them what they can do since you can barely talk from the pain "
             "They tell you that if they can join you on your adventure, then they would "
             "give you the antidote.", speed)

#9  #Adds to the choices list        
    choices.extend(('trust', 'not'))
    decision_9 = input("Do you trust them or not?" 
                       "(Trust, not) ").lower().strip()
    while decision_9 not in choices:
        print('Just one of the options')
        decision_9 = input("Do you trust them or not?" 
                           "(Trust, not) ").lower().strip()

    if decision_9 == 'trust':
        prints_t("Skye meets your gaze and sees that you want to trust them so "
                 "your team chooses to trust the enemies who end up giving you the antidote "
                 "and within munites, the pain subsides and you geu up ont oyur feet again", speed)
        group.append('trust')
        
    elif decision_9 == 'not':
        prints_t("\nSkye sees the distrust in your eyes but couldn't bear to see you die "
                 'so she decides to trust them and gets the antidote which heals you in seconds '
                 "she apologises to you but tells you her reasoning and you tell her that "
                 "you don't blame her for her choice", speed)
        group.append('distrust')
        
    choices.clear()
    choice11()

#This one is for when you're taken and need to either escape or wait for something
def choice10():
    prints_t("\nThe enemies tie up your hands and take you hostage to their village. "
             "You are taken to a prison where you wait until the leader is ready "
             "You still have your dagger in your boots, do you try to escape?", speed)
    time.sleep(0.5)
    prints_t('Your inventory has:\n', speed)
    for item, desc in inventory.items():
        print(f'{item}: {desc}')
        
#10 #Adds to the choices list        
    choices.extend(('escape', 'wait'))
    decision_10 = input("\nDo you?" 
                       "(Escape, Wait) ").lower().strip()
    while decision_10 not in choices:
        print('Just one of the options')
        decision_10 = input("\nDo you?" 
                            "(Escape, Wait) ").lower().strip()

    if decision_10 == 'escape':
        prints_t("\nYou covertly take out your dagger and free yourself from the shackles"
                 "you then free your team too and try to think of a way to escape the prison "
                 "Skipp tells you that he could cut through the walls with your dagger if "
                 "you give him enough mana from yourself.", speed)
        choice12()
        
    elif decision_10 == 'wait':
        prints_t("\nYou go against your better judgement and decide to wait before freeing yourself "
                 'as it turns out, it was rhe right call because the assassin from earlier came back to help you. '
                 'They give you your equipment and provisions and you all escape the village towards Wynn ', speed)
        group.append('high trust')
        choice11()
    choices.clear()

#This one is for when you're in the cave and need to either defend or doge
def choice11():
    prints_t(f"\nYour team is now larger with {group[0]} "
             "you pass the forest and find a cave that you need to venture into, along the way "
             "you try to get to know the new members of your team, you find out the assassin's name is "
             "Cupz and the archer's name is Mugz, you tried to inquire as to how they got their "
             "names but you were interrupted by a loud roar in the cave", speed)
    prints_t("\nYour team preapares for a fight with a monster but it turns out that it was just a "
             "relatively small cat with a powerful voice, Skye says she wants to bring it with you "
             "but Skipp warns her that it didn't have a poerful voice for no reason, and that it had the power "
             "and speed in its small stature to kill a party of 7 if it's underestimated. "
             "Because of all of your commotion, the cat spots your team and charges.", speed)

#11 #Adds to the choices list        
    choices.extend(('defend', 'doge'))
    decision_11 = input("\nDo you try to defend yourself or try to doge it?" 
                       "(Defend, Doge) ").lower().strip()
    while decision_11 not in choices:
        print('Just one of the options')
        decision_11 = input("\nDo you try to defend yourself or try to doge it?" 
                            "(Defend, doge) ").lower().strip()

    if decision_11 == 'doge':
        prints_t("\nYou doge out of the way right in time to not get hit with the cat's claws but you see it "
                 "slice through a solid rock, which scares you a little "
                 "Skipp luckily binds it which allows you to het up close and examine its calws... ", speed)
        
    elif decision_11 == 'defend':
        prints_t("\nYou try to defnd yourself with a large nearby rock but the cat slices right through it "
                 'and into your flesh ', speed)
        prints_t("\nIt deals a fatal wound and you collapse from exhaustion "
                 "You wake up back in the kingdom and decide that you're not cut out for adventures "
                 "You live the rest of your life, never discovering the mysteries of Wynn...", speed)
#11.5   #Adds to the choices list
        choices.extend(('quit', 'replay'))
        decision_11_5 = input("\nDo you want to leave or replay?" 
                            "(Quit, Replay) ").lower().strip()
        while decision_11_5 not in choices:
            print('Just one of the options')
            decision_11_5 = input("\nDo you want to leave or replay?" 
                                "(Quit, Replay) ").lower().strip()

        if decision_11_5 == 'quit':
            quit()     
        
        elif decision_11_5 == 'replay':
            main()
            
    choices.clear()
    choice13()

#This one is for if you want to trust Skipp or if you want to wait it out
def choice12():
    prints_t("\nYou vaguely remember Skipp teaching you how to channel your mana into another being "
             "but you were only half-listening at the time...", speed)
    prints_t("\nBut Skye encourages you and even offers to help Skipp herself "
             "hearing that made you confident and convinced you that you could do it "
             "with her help.", speed)
    
#12 #Adds to the choices list        
    choices.extend(('try', 'wait'))
    decision_12 = input("\nDo you try to escape now or wait for a better chance of escape?" 
                        "(Try, Wait) ").lower().strip()
    while decision_12 not in choices:
        print('Just one of the options')
        decision_12 = input("\nDo you try to escape now or wait for a better chance of escape?" 
                            "(Try, Wait) ").lower().strip()

    if decision_12 == 'try':
        prints_t("\nYou believe in Skipp and try your hardest to channel mana into him "
                 "slowly, fist with cracks then chunks that fall, the wall breaks and you get to flee "
                 "Your team manages to find some supplies and your weapons right outside the prison "
                 "so you take whatever you could and run out of there.", speed)
        prints_t("You now have lesser provisions but still enough to survive", speed)
        choice16()

    elif decision_12 == 'wait':
        prints_t("\nYou decide against the plan and instead wait until someone comes by so that you can run out "
                 'right as soon as you hear someone opening the door, you ready yourself fo fight '
                 "but you get knocked out and carried away with your gear, as it turns out, "
                 "they just needed your map but they realized that you were stronger than they were "
                 "so they recruited your help to get to Wynn", speed)
        choice15()
    choices.clear()
    
#This one is for the cute cat
def choice13():
    prints_t("\nThe cat's claws seem to be made mostly of iron and be as sharp as razors"
             "But now...the hardest decision yet, will you pet it?", speed)
#13 #Adds to the choices list        
    choices.extend(('pet', 'hold back'))
    decision_13 = input("\nYou know that it's deadly but it just looks so cute.." 
                        "(Pet, Hold back) ").lower().strip()
    
    while decision_13 not in choices:
        print('Just one of the options')
        decision_13 = input("\nYou know that it's deadly but it just looks so cute.." 
                            "(Pet, Hold back) ").lower().strip()

    if decision_13 == 'pet':
        prints_t("\nYou can't hold back anymore and pet the cute cat "
                 "surprisingly, it's affectionate and recieves the pets well ", speed)
        prints_t("You decide to free the cat safely and continue onward", speed)
        choice17()

    elif decision_13 == 'hold back':
        prints_t("\nYou somehow manage to refrain from petting the cat (because you're a monster >:( ) "
                 'and decide to set it free back into the winderness, you continue onward until', speed)
        choice20()

#This one is for the cave without the other two
def choice14():
    prints_t("\nYou continue your journey onward, finding various treasures and plants along the way. "
             "When you enter a cave, you encounter a tiny beast that, despite its stature, could decimate an entire party "
             "You cautiously approach it and are surprisingly able to pet it. Up close you see that it looks like a "
             "blind badger mole which Skipp tells you are great at detecting intention and are adorable", speed)
    prints_t("\nAfter petting it, it seemed like it was gesturing for you to follow it, so you do so"
             "You find a sleeping mega-bear along the way, and fearful that it may wake up and attack, "
             "you wonder if you should kill it while it's asleep", speed)

#14 #Adds to the choices list        
    choices.extend(('attack', 'continue'))
    decision_14 = input("\nWhat do you think is right? " 
                        "(attack, continue) ").lower().strip()
    while decision_14 not in choices:
        print('Just one of the options')
        decision_14 = input("\nWhat do you think is right? To attack a defenseless animal or to continue onward? " 
                            "(attack, continue) ").lower().strip()

    if decision_14 == 'attack':
        prints_t("\nYou decide to attack the sleeeping mega-bear which, as it turns out "
                 "has a hide made of steel, it angrily wakes up and kills you and your party"
                 "(To be fair...it was deserved, killing a sleeping animal? cowardly...)", speed)
        death()

    elif decision_14 == 'continue':
        prints_t("\nYou continue onwards, following the badger mole until you finally reach your destination.. ", speed)
        choice20()
    choices.clear()

#This is for when your recruited to go to Wynn
def choice15():
    prints_t("You reluctantly take back your gear and follow the new leader of the party. "
             "You don't like how they all seem to be relying on you, so you devise a plan with "
             "Skipp and Skye to take the map and run away, the only problem is, who would be "
             "fast enough to take tha map AND run away")

#15 #Adds to the choices list        
    choices.extend(('me', 'skye'))
    decision_15 = input("\nWho do you think should take the map? Myself(you) or Skye? " 
                        "(Me, Skye) ").lower().strip()
    while decision_15 not in choices:
        print('Just one of the options')
        decision_15 = input("\nWho do you think should take the map? Myself(you) or Skye? " 
                            "(Me, Skye) ").lower().strip()

    if decision_15 == 'me':
        prints_t("\nYou try to snatch the map but you were too slow and were apprehended "
                 "and then killed because the rest of the team ran away", speed)
        death()

    elif decision_15 == 'skye':
        prints_t("\nYou entrust Skye with taking the map from the leader. "
                 "On her signal, you and Skipp run away into the woods as fast as possible "
                 "Skye eventually catches up to you two and a chase ensues which only lasts a few "
                 "minutes before finally, you escape the captors."
                 "After catching your breaths and taking a quick break, you continue your journey "
                 "to Wynn", speed)
    choices.clear()
    choice14()

#This is for when you're free but with fewer provisions
def choice16():
    prints_t("Although you have lesser provisions, you still managed to scrounge up some berries "
             "and hunt wild animals to stay alive", speed)
    prints_t("While surviving, Skye asks the crucuial question", speed)
#16 #Adds to the choices list        
    choices.extend(('wynn', 'home'))
    decision_16 = input("\nDo we keep going for Wynn or do we go home? " 
                        "(Wynn, Home) ").lower().strip()
    while decision_16 not in choices:
        print('Just one of the options')
        decision_16 = input("\nDo we keep going for Wynn or do we go home? " 
                            "(Wynn, Home) ").lower().strip()

    if decision_16 == 'home':
        prints_t("\nYou you decide to head towards home and forget about your adventures and continue "
                 "living your lives from before the adventure happened...", speed)
#16.5   #Adds choices to the list 
        choices.extend(('quit', 'replay'))
        decision_16_5 = input("\nDo you want to leave or replay?" 
                            "(Quit, Replay) ").lower().strip()
        while decision_16_5 not in choices:
            print('Just one of the options')
            decision_16_5 = input("\nDo you want to leave or replay?" 
                                "(Quit, Replay) ").lower().strip()

        if decision_16_5 == 'quit':
            quit()     
        
        elif decision_16_5 == 'replay':
            main()
            
    elif decision_16 == 'wynn':
        prints_t("\nYou decide to head towards Wynn, knowing that with determination and "
                 "your survival skills, you can make it to Wynn "
                 "after a few weeks of trudging through the various terrain,", speed)
    choices.clear()
    choice20()

#This is for if you choose to pet the cat
def choice17():
    prints_t("\nAs it turns out, the cat wasn't alone and returned later on in the path with friends "
             "At first you were apprehensive but then it felt like you were on cloud 9, "
             "with your party, you all spent time petting the cats along your journey until "
             "you reached a fork in the road but the cats seemed to know where they were going ", speed)
    
#17 #Adds to the choices list        
    choices.extend(('follow', 'no'))
    decision_17 = input("\nDo you follow the cats? " 
                        "(follow, no) ").lower().strip()
    while decision_17 not in choices:
        print('Just one of the options')
        decision_17 = input("\nDo you follow the cats? " 
                            "(follow, no) ").lower().strip()

    if decision_17 == 'follow':
        prints_t("\nYou make the right call and follow the cats all the way until ", speed)

    elif decision_17 == 'no':
        prints_t("\nYou decide to not follow the cats which prompted them to follow you instead. "
                 "Turns out, the path only diverged for a little bit before re-merging again, "
                 "either way, it still led you with your team and", speed)
    
    choices.clear()
    choice20()

#This is for when you finally make it into Wynn
def choice20():
    prints_t("\nYou finally make it to Wynn and find out that its mysteries are the animlas that you have encountered "
             "along your journey, along with the huge haul of riches you've found. "
             "Your team decides to get some of the riches that they could carry and to keep the existence "
             "of the animals safe.", speed)
    end()
    time.sleep(2)
#20 #Adds to the choices list
    choices.extend(('quit', 'replay'))
    decision_20 = input("\nDo you want to leave or replay?" 
                        "(Quit, Replay) ").lower().strip()
    while decision_20 not in choices:
        print('Just one of the options')
        decision_20 = input("\nDo you want to leave or replay?" 
                            "(Quit, Replay) ").lower().strip()

    if decision_20 == 'quit':
        quit()     
        
    elif decision_20 == 'replay':
        main()

#This one is for when you either trust your team or confront the assassin
def tree_s():
    while True:    
        choice6()
#6      #Adds to the choices list
        choices.extend(('trust', 'confront'))
        decision_6 = input("\nTrust your team to defend you or turn "
                           "around and confront the Assassin "
                           "(Trust, Confront) ").lower().strip()

        while decision_6 not in choices:
            print("Just one of the two")
            decision_6 = input("\nTrust your team to defend you or turn "
                               "around and confront the Assassin"
                               "(Trust, Confront) ").lower().strip()
    
        if decision_6 == 'trust':
            prints_t("\nSkye jumps in right on time to catch the assassin "
                     "off guard and she pins him to the ground as Skipp uses "
                     "his binding spell to keep them in place", speed)

        elif decision_6 == 'confront':
            choices.clear()
            choice8()
        choices.clear()

#Theis one is for when you either jump in to save Skye or trust her to survive
def rock_s():
    while True:
        choice7()
#7      #Adds to the choices list
        choices.extend(('trust', 'run'))
        decision_7 = input("\nTrust her to survive or run in and try "
                           "to defend her(Trust, Run) ").lower().strip()
        while decision_7 not in choices:
            print("Just one of the two")
            decision_7 = input("\nTrust her to survive or run in and try "
                               "to defend her(Trust, Run) ").lower().strip()

        if decision_7 == 'trust':
            prints_t("\nSkye holds the assassin she caught to defend herself "
                     "the assassin gets hit in the leg and yells out in pain "
                     "turns out, the arrow was dipped in some kind of poison "
                     "The assassin knew of it and that's why he yelled", speed)
            prints_t("\nThe archer flees, leaving their teammate to die in the wild...", speed)
            prints_t("\nYour team collectively decide to continue to Wynn, leaving the injured assassin"
                     "along with some provisions", speed)
            choice14()
            
        elif decision_7 == 'run':
            choices.clear()
            choice9()

        choices.clear()

#The main function for the story
def main():
    #This keeps the story funning indefinitely
    while True:
        #Starts and shows the first choice
        start()
        choice1()
#1      #Adds initial choices for the first decision
        choices.extend(('yes', 'no'))
        starting_decision = input("\nDo you want to embark on an adventure? ").lower().strip()

        while starting_decision not in choices:
            print('Just one of the options: yes or no')
            starting_decision = input("\nDo you want to embark on an adventure? ").lower().strip()

        if starting_decision == 'no':
            prints_t("Aw, ok...I will still leave though, this is a once in a lifetime opportunity", speed)
            prints_t("\nYou see Skipp the next day embarking on his adventure, never seeing him again...", speed)
            quit()
        elif starting_decision == 'yes':
            prints_t("\nAlright! Let's find the Treasures and solve the Mysteries of Wynn", speed)
            choices.clear()

        choice2()
        #Tells the player of the things in their inventory
        prints_t('\n\nYou have a sword, a dagger, a health potion, a strength potion, '
                 'and unbreaking runes to strengthen your clothing.', speed)
        #Adds to the inventory dictionary
        inventory['Sword'] = 'Your trusty sword that you have had for years.'
        inventory['Dagger'] = 'A concealed dagger that is in your boot.'
        inventory['Potions'] = {'healing' : 'A potion that heals you.',
                               'strength' : 'A potion that strengthens you.'}
        inventory['Runes'] = 'Unbreaking Runes that make your clothing strong as armor'
#2      #Adds to the choices list
        choices.extend(('convince', 'not'))
        decision_2 = input("\nDo you try to convince him to leave some stuff behind?"
                           "(convince, not) ").lower().strip()
        #Keeps asking the player until they input a valid answer
        while decision_2 not in choices:
            print("That's not a valid option")
            decision_2 = input("\nDo you try to convince him to leave some stuff behind?"
                               "(convince, not) ").lower().strip()

        if decision_2 == 'convince':
            prints_t("\nYou tell Skipp that that's way too much stuff "
                     "but Skipp argues against you, and somehow convinces you to let him bring "
                     "his stuff anyways, and somehow also convinces you to carry some of the stuff, "
                     "by telling you he'll take most of the stuff himself.", speed)
        elif decision_2 == 'not':
            prints_t("\nSkipp readily agrees with you, so you both decide to share the stuff, "
                     "him carrying a bit more, obviously.", speed)
        choices.clear()

        print("You now have provisions that will last you the rest of the adventure.")
        inventory['provisions'] = 'Enough food and drinks to last for the whole adventure'
        
        choice3()
#3      #Adds to the choices list
        choices.extend(('yes', 'no'))
        decision_3 = input("\nYeah why not or No, it's probably useless "
                           "(yes, no) ").lower().strip()
        #Keeps asking the player until they input a valid answer
        while decision_3 not in choices:
            print("Invalid option: yes or no")
            decision_3 = input("\nYeah why not or No, it's probably useless "
                               "(yes, no) ").lower().strip()

        if decision_3 == 'yes':
            prints_t("\nYou decide to take the ring, let's just hope that was the right choice..", speed)
            inventory['strange ring'] = 'A strange glowing ring that emits a mysterious energy'
        elif decision_3 == 'no':
            prints_t("\nYou decide to leave the ring on the ground, that may have been the right decision", speed)
        choices.clear()
    
        choice4()
#4      #Adds to the choices list
        choices.extend(('tell', 'no'))
        decision_4 = input('\nDo you tell the others? '
                           '(tell, no) ').lower().strip()
        #Keeps asking the player until they input a valid answer
        while decision_4 not in choices:
            print("Just one of the options: tell or no")
            decision_4 = input('\nDo you tell the others? '
                               '(tell, no) ').lower().strip()

        if decision_4 == 'tell':
            prints_t('\nYou covertly whisper to your team that you see someone following close behind,'
                     'so Skye readies her blade and Skipp prepares his smokescreen, and binding spells, '
                     'on your signal, they yell out, turn around and attack whatever you do,', speed)
        elif decision_4 == 'no':
            prints_t('\nYou continue onward into the woods, disregarding your thoughts, as you descend '
                     'into a ravine, you and your party get shot down while traveling along a steep cliff, '
                     'turns out somebody was indeed watching you...', speed)
            death()
        choices.clear()

        choice5()
#5      #Adds to the choices list
        choices.extend(('tree', 'rock'))        
        decision_5 = input("\nBehind a tree in the distance or behind a rock close to Skye?"
                           "(Tree, Rock) ").lower().strip()
        #Keeps asking the player until they input a valid answer        
        while decision_5 not in choices:
            print("Either the tree or the rock")
            decision_5 = input("\nBehind a tree in the distance or behind a rock close to Skye?"
                               "(Tree, Rock) ").lower().strip()

        if decision_5 == 'tree':
            prints_t("\nYou approach a tree, and try to restrain whatever's behind it, "
                     "without hurting it too much.", speed)
            tree_s()

        elif decision_5 == 'rock':
            prints_t("\nYou gesture to Skye to attack behind the rock, "
                     "so she does so and apprehends someone who seems to be an assassin", speed)
            rock_s()
        choices.clear()

main()