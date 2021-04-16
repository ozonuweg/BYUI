"""
File: prove06.py
Prove: 06
Topic: Adventure Game
Author: Glory Ozonuwe

Purpose: In a text-based adventure game, the user is presented a scenario with different options. 
Depending on the option they choose, they have different consequences, which in turn present 
different choices for the next action.
"""

print()
#Introduction 
print("You're about to enter the headquaters of your arch nemesis.")
print("The mission is to acquire a stolen gold from the target.")
print("You need a code name for this mission.")

#Get code name
code_name = input("What is it? ")
code_name = code_name.title()

#Confirm code name
print("Your code name is confirmed to be " + code_name + ". Good luck!")

#Start Mission
print()
print()
print("At the front of the imposing building, you see a weathered old man with a cart filled with junk " +
"and a few useful items. All you have on you is a jar of water. What do you want to do with it?")
print("-> GIVE")
print("-> KEEP")
first_choice = input(code_name + ", what is your choice? ")
print()

if first_choice.lower() == "give":
    print("You offer it to him, and he says he’ll trade a flashlight or a bobble pin to you.")
    print("-> FLASHLIGHT")
    print("-> BOBBY PIN")
    second_choice = input("Hmmm... you have to choose wisely " + code_name + ". ")
    print()

    if second_choice.lower() == "flashlight":
        print("You go through the back door and it's dark. Good Choice you made earlier, " + code_name + ". You bring out the " +
        "flashlight and turn it on. You can clearly see your target but you have to be careful so you don't " +
        "tip him off. You need the gold with him. Capture or confront him? ")
        print("-> CAPTURE")
        print("-> CONFRONT")
        third_choice = input("> ")
        print()

        if third_choice.lower() == "capture":
            print("SUCEESS! You quietly captured him and took the gold from him. He wasn't able to get help on time. ")
            print("YOU WON! Game Over.")
            print()

        elif third_choice.lower() == "confront":
            print("Wrong move " + code_name + ". You have created a scene. His bodyguards caught you arguing with him. You forgot you're in his " +
            "territory and he has eyes everywhere. He alerted them and you're now an hostage. :)")
            print("GAME OVER! You Lost!")
            print()

        else:
            print("You have to select from the option! Run program again.")
            print()
    
    elif second_choice.lower() == "bobby pin":
        print("Not a bad choice, " + code_name + ". Let's see how helpful that is. You go through the back door and it's dark. " +
        "You don't have a flashlight or a candle. You touch the walls and you feel a switch. Do you want to turn it on or not? ")
        print("-> TURN ON")
        print("-> LEAVE IT OFF")
        choice_2b = input("> ")
        print()

        if choice_2b.lower() == "turn on":
            print("NOOOOO! You just drew attention to yourself. Everyone is staring at you and now target is no where to be found.")
            print("Sorry, GAME OVER! " + code_name)
            print()

        elif choice_2b.lower() == "leave it off":
            print("You walked blindly into the main hall and hear music blasting. You quickly scan the place and you can see your target. " + 
            "With the bobby pin, you open the safe to his room and find the gold. YAY! ")
            print("Mission Accomplished! Gold Found. GAME OVER.")
            print()

        else:
            print("You have to select from the option! Run program again.")
            print()

    else:
        print("You have to select from the option! Run program again.")
        print()



elif first_choice.lower() == "keep":
    print("You decide to keep your water and he walks away. You proceed into the building " +
    "and see your target. Do you want to approach or lay low?")
    print("-> APPROACH")
    print("-> LAY LOW")
    sub_choice = input("What will it be " + code_name + "? ")
    print()

    if sub_choice.lower() == "approach":
        print("You approach the target and introduce yourself as a big fan who wants to take a picture with him. " +
        "He clearly doesn't know you but decides to honor your request. His bodyguards are a bit protective and decides to search you first " + 
        "Will you AGREE to their request or SCREAM for help? ")
        last_choice = input("> ")
        print()

        if last_choice.lower() == "agree":
            print("SUCEESS! They searched and found just your jar of water. The target offered you a drink in his room for the incovenience " +
            "You stole the gold when he wasn't paying attention and left the room successfully.")
            print("YOU WON! " + code_name + " Game Over.")
            print()

        elif last_choice.lower() == "scream":
            print("Wrong move " + code_name + ". You have created a scene. His bodyguards were at alert. They quickly took the target " +
            "away for his safety and kicked you out.")
            print("GAME OVER! You Lost!")
            print()

        else:
            print("You have to select from the option! Run program again.")
            print()
    
    elif sub_choice.lower() == "lay low":
        print("Not a bad choice, " + code_name + ". Let's see how helpful that is. You disguise yourself as a room service agent. " +
        "You have a bodyguard watching you as you enter the target's room to clean it up. You have found the gold. You can either JUMP through the window " +
        "or HIDE the gold in the cleaning equipments.")
        final_choice = input("> ")
        print()

        if final_choice.lower() == "jump":
            print("NOOOOO! You just fell and died.")
            print("Sorry, GAME OVER! " + code_name)
            print()

        elif final_choice.lower() == "hide":
            print("You quickly leave the room rolling out the cleaning equipment. The bodyguard at the door searches you but finds just your jar of water. " +
            "You head to the back and leave the building. YAY! ")
            print("Mission Accomplished! Gold Found. GAME OVER.")
            print()

        else:
            print("You have to select from the option! Run program again.")
            print()

    else:
        print("You have to select from the option! Run program again.")
        print()


else:
    print("You have to select from the option! Run program again.")
    print()