import json
import time
import random
import sys
inventoryslot1 = "empty"
inventoryslot2 = "empty"
inventoryslot3 = "empty"
inventoryslot4 = "empty"
inventoryslot5 = "empty"
inventoryslot6 = "empty"
inventoryslot7 = "empty"
inventoryslot8 = "empty"
inventoryslot9 = "empty"
inventoryslot10 = "empty"
inventoryslot11 = "empty"
inventoryslot12 = "empty"
inventoryslot13 = "empty"
inventoryslot14 = "empty"
inventoryslot15 = "empty"
inventoryslot16 = "empty"
inventoryslot17 = "empty"
inventoryslot18 = "empty"
inventoryslot19 = "empty"
inventoryslot20 = "empty"
pet = "none"
houselevel = 0
justfound = "nothing"
item1name = ""
item2name = ""
item1 = None
item2 = None
diamondflowerstatus = False
hatslot = "empty"
shoesslot = "empty"
diamondbouquetstatus = False
debug = False
def main():
    global justfound, pet, houselevel, item1, item2, item1name, item2name, diamondflowerstatus, hatslot, shoesslot, diamondbouquetstatus, debug
    whatdoyoudo = input("what do you want to do? (type 'help' for a list of commands): ")
    if whatdoyoudo == "help": # help command, shows a list of commands
        print("help - shows this message")
        print("inventory [1-20] - shows your inventory")
        print("use [1-20] - uses an item in your inventory")
        print("tree - find a tree")
        print("rock - find a rock")
        print("flower - find a flower")
        print("sand - find some sand")
        print("pickup - picks up what ever you just found")
        print("drop [1-20] - drops an item in your inventory")
        print("move [1-20] [1-20] - moves an item from one inventory slot to another")
        print("craft [1-20] [1-20] - crafts an item in one slot with an item in another slot")
        print("exit - exits the game")
        print("save - saves the game")
        print("load - loads a save")
        if pet != "none" or debug:
            print("pet - shows your pet")
            print("petrelease - releases your pet")
        if debug:
            print("reset diamond bouquet - resets the diamond bouquet and makes the diamond flower unactive")
            print("reset diamond flower - resets the diamond flower and makes it unactive")
            print("reset house - resets your house level to 0 and makes you have no house")
            print("reset pet - resets your pet to none and releases your pet if you have one")
            print("reset inventory - resets your inventory and makes all inventory slots empty")
            print("reset all - resets all progress, including pet, house level, inventory, and all other progress")
            print("debug - toggles debug mode, which shows debug commands and allows you to use debug commands if it is on")
            print("giveitem [name] - gives you an item, only works in debug mode")
        print("hat - shows your hat")
        print("shoes - shows your shoes")
    elif whatdoyoudo.startswith("inventory "): # inventory [1-20] - shows your inventory
        slot = whatdoyoudo.split(" ")[1]
        if slot.isdigit() and 1 <= int(slot) <= 20:
            print(globals().get(f"inventoryslot{slot}"))
        else:
            print("Invalid inventory slot. Please enter a number between 1 and 20.")
    elif whatdoyoudo.startswith("use "): # use [1-20] - uses an item in your inventory
        slot = whatdoyoudo.split(" ")[1]
        if slot.isdigit() and 1 <= int(slot) <= 20:
            item = globals().get(f"inventoryslot{slot}")
            if item == "empty":
                print("That slot is empty.")
            elif item == "rock":
                print("You throw the rock. It breaks and you find a gem inside!")
                justfound = "gem"
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "flower":
                print("You smell the flower. It smells like roses, but you drop it.")
                globals()[f"inventoryslot{slot}"] = "empty"
                justfound = "flower"
            elif item == "wood":
                print("You use the wood to make a house.")
                justfound = "nothing"
                houselevel == 1
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "gem":
                print("You use the gem and it leads you to a hidden treasure! but then breaks.")
                justfound = "treasure box"
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "treasure box":
                print("You open the treasure box and find a diamond ore inside!")
                justfound = "diamond ore"
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "magic wand":
                print("You wave the magic wand and it turns into a rabbit!")
                justfound = "a rabbit"
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "stone pickaxe":
                mine(pickaxetype="stone")
            elif item == "iron pickaxe":
                mine(pickaxetype="iron")
            elif item == "diamond pickaxe":
                mine(pickaxetype="diamond")
            elif item == "gold pickaxe":
                mine(pickaxetype="gold")
            elif item == "emerald pickaxe":
                mine(pickaxetype="emerald")
            elif item == "ruby pickaxe":
                mine(pickaxetype="ruby")
            elif item == "mythril pickaxe":
                mine(pickaxetype="mythril")
            elif item == "adamantite pickaxe":
                mine(pickaxetype="adamantite")
            elif item == "a rabbit":
                print("You pet the rabbit. It seems happy and becomes your pet.")
                justfound = "nothing"
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "a rabbit"
            elif item == "bouquet":
                if pet != "none":
                    print("You give the bouquet to your pet, your pet seems to like it.")
                    justfound = "nothing"
                    globals()[f"inventoryslot{slot}"] = "empty"
                else:
                    print("You smell the bouquet, it smells very nice. you wish you could give it to a pet.")
            elif item == "diamond bouquet":
                if pet != "none":
                    print("You give the diamond bouquet to your pet, your pet seems to really like it. they think its the best thing ever and they will never leave your side now. and will protect you at all costs.")
                    justfound = "nothing"
                    globals()[f"inventoryslot{slot}"] = "empty"
                    diamondflowerstatus = True
                    while diamondbouquetstatus:
                        diamondflowerstatus = True
                else:
                    print("You smell the diamond bouquet, it smells very nice. you wish you could give it to a pet.")
            elif item == "boulder":
                print("You try to use the boulder, but it's too heavy and you accidently drop it on your foot. you lose all your items and die.")
                if diamondflowerstatus and pet != "none":
                    print("but your pet revives you because of the diamond flower")
                else:
                    sys.exit()
            elif item == "big gem":
                print("You use the big gem and it leads you to a hidden treasure!")
                justfound = "treasure box"
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "a magic rabbit":
                print("You pet the magic rabbit. It seems happy and becomes your pet.")
                justfound = "nothing"
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "a magic rabbit"
            elif item == "glasses":
                print("You put on the glasses and your coolness level increases by 1000!")
                globals()[f"inventoryslot{slot}"] = "empty"
                hatslot = "glasses"
            elif item == "a cool rabbit":
                print("You pet the cool rabbit. It seems happy and becomes your pet. it also thanks you for making it cool.")
                justfound = "nothing"
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "a cool rabbit"
            elif item == "a cool magic rabbit":
                print("You pet the cool magic rabbit. It seems happy and becomes your pet. it also thanks you for making it cool.")
                justfound = "nothing"
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "a cool magic rabbit"
            elif item == "coal" or item == "iron ore" or item == "gold ore" or item == "diamond ore" or item == "emerald ore" or item == "ruby ore" or item == "sapphire ore" or item == "evil ore" or item == "mythril ore" or item == "adamantite ore":
                print("you cannot use a mineral, it can only be crafted with other items")
            elif item == "sand":
                print("you play with the sand for a bit")
            elif item == "glass":
                if houselevel == 1:
                    print("you use the glass to make a window for your house")
                    justfound = "nothing"
                    globals()[f"inventoryslot{slot}"] = "empty"
                    houselevel = 2
                else:
                    print("you look at the glass but dont know what to do with it.")
            elif item == "mystics cat":
                print("You pet mystics cat, it seems happy and becomes your pet. it also tells you about a game called geometry dash and how they play it a lot.")
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "mystics cat"
            elif item == "diamond flower":
                if pet == "none":
                    print("you cannot use the diamond flower without a pet, it just looks pretty in your inventory.")
                else:
                    if diamondflowerstatus:
                        print("you undo the effect of the diamond flower, your pet can now be released and your pet cannot revive you if you die, also your pet doesnt look as pretty anymore.")
                    else:
                        print("you use the diamond flower on your pet to be unable to be released, it also makes your pet able to revive you if you die, also your pet looks very pretty.")
                        diamondflowerstatus = True
            elif item == "mystics cat":
                print("You pet mystics cat, it seems happy and becomes your pet. it also tells you about a game called geometry dash and how their previous owner played it a lot.")
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "mystics cat"
            elif item == "a axolotl":
                print("You pet the axolotl, it seems happy and becomes your pet.")
                globals()[f"inventoryslot{slot}"] = "empty"
                if pet == "none":
                    pet = "a axolotl"
            else:
                print(f"the item you are using is unknown, the item is being deleted incase you cheated it in or something.")
                justfound = "nothing"
                globals()[f"inventoryslot{slot}"] = "empty"
        else:
            print("Invalid inventory slot. Please enter a number between 1 and 20.")
    elif whatdoyoudo.startswith("drop "): # drop [1-20] - drops an item in your inventory 
        slot = whatdoyoudo.split(" ")[1]
        if slot.isdigit() and 1 <= int(slot) <= 20:
            if globals().get(f"inventoryslot{slot}") == "empty":
                print("That slot is already empty.")
            else:
                print(f"You drop the {globals().get(f'inventoryslot{slot}')}, type 'pickup' to pick it up again.")
                justfound = globals().get(f"inventoryslot{slot}")
                globals()[f"inventoryslot{slot}"] = "empty"
        else:
            print("Invalid inventory slot. Please enter a number between 1 and 20.")
    elif whatdoyoudo == "tree": # tree - find a tree, but there is a small chance to find mystics cat instead of wood
        if random.randint(1, 100) <= 3:
            print("You find a tree, but you see a cat just chilling near it")
            justfound = "mystics cat"
        else:
            print("You find a tree, you break it and find some wood!")
            justfound = "wood"
    elif whatdoyoudo == "rock": # rock - find a rock
        print("You find a rock!")
        justfound = "rock"
    elif whatdoyoudo == "sand": # sand - find some sand
        print("You find some sand!")
        justfound = "sand"
    elif whatdoyoudo == "flower": # flower - find a flower
        print("You find a flower!")
        justfound = "flower"
    elif whatdoyoudo == "pickup": # pickup - picks up what ever you just found
        if justfound == "nothing":
            print("There is nothing to pick up.")
        elif justfound == "evil ore":
            print("You pick up evil ore")
            print("what do you want to do? (type 'help' for a list of commands): ")
            time.sleep(2)
            print("you cant seem to type...")
            time.sleep(1)
            print("the evil ore fills you with darkness and you lose all your items and die")
            if diamondflowerstatus and pet != "none":
                print("but your pet revives you because of the diamond flower")
            else:
                sys.exit()
        else:
            for i in range(1, 21):
                if globals().get(f"inventoryslot{i}") == "empty":
                    globals()[f"inventoryslot{i}"] = justfound
                    print(f"You pick up the {justfound}.")
                    print(f"it was placed in slot {i}")
                    justfound = "nothing"
                    break
            else:
                print("Your inventory is full. You can't pick up the item.")
    elif whatdoyoudo.startswith("move "): # move [1-20] [1-20] - moves an item from one inventory slot to another
        parts = whatdoyoudo.split(" ")
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            from_slot = int(parts[1])
            to_slot = int(parts[2])
            if 1 <= from_slot <= 20 and 1 <= to_slot <= 20:
                if globals().get(f"inventoryslot{from_slot}") == "empty":
                    print("The source slot is empty. There's nothing to move.")
                elif globals().get(f"inventoryslot{to_slot}") != "empty":
                    print("The destination slot has a item in it, you can't move an item to a slot that isn't empty.")
                else:
                    globals()[f"inventoryslot{to_slot}"] = globals().get(f"inventoryslot{from_slot}")
                    globals()[f"inventoryslot{from_slot}"] = "empty"
                    print(f"You moved the item from slot {from_slot} to slot {to_slot}.")
            else:
                print("Invalid inventory slots. Please enter numbers between 1 and 20.")
        else:
            print("Invalid command format. Use 'move [from] [to]' with valid slot numbers.")
    elif whatdoyoudo.startswith("craft "): # craft [1-20] [1-20] - crafts an item in one slot with an item in another slot
        parts = whatdoyoudo.split(" ")
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            item1 = int(parts[1])
            item2 = int(parts[2])
            if 1 <= item1 <= 20 and 1 <= item2 <= 20:
                if globals().get(f"inventoryslot{item1}") == "empty" and globals().get(f"inventoryslot{item2}") == "empty":
                    print("Both slots are empty. you need 2 items to craft.")
                else:
                    if globals().get(f"inventoryslot{item1}") == "empty":
                        print("The first slot is empty. you need 2 items to craft.")
                    elif globals().get(f"inventoryslot{item2}") == "empty":
                        print("The second slot is empty. you need 2 items to craft.")
                    else:
                        item1name = globals().get(f"inventoryslot{item1}")
                        item2name = globals().get(f"inventoryslot{item2}")
                        crafted_any = (
                            crafting("wood", "gem", "magic wand") or
                            crafting("wood", "rock", "stone pickaxe") or
                            crafting("wood", "iron ore", "iron pickaxe") or
                            crafting("wood", "diamond ore", "diamond pickaxe") or
                            crafting("wood", "gold ore", "gold pickaxe") or
                            crafting("wood", "emerald ore", "emerald pickaxe") or
                            crafting("wood", "ruby ore", "ruby pickaxe") or
                            crafting("wood", "mythril ore", "mythril pickaxe") or
                            crafting("wood", "adamantite ore", "adamantite pickaxe") or
                            crafting("pi", "pi", "this line of code is pi cause this is the 314th line") or
                            crafting("a rabbit", "gem", "a magic rabbit") or
                            crafting("flower", "flower", "bouquet") or
                            crafting("rock", "rock", "boulder") or
                            crafting("gem", "gem", "big gem") or
                            crafting("wood", "glass", "glasses") or
                            crafting("a rabbit", "glasses", "a cool rabbit") or
                            crafting("a magic rabbit", "glasses", "a cool magic rabbit") or
                            crafting("coal", "sand", "glass") or
                            crafting("a cool rabbit", "gem", "a cool magic rabbit") or
                            crafting("diamond ore", "flower", "diamond flower") or
                            crafting("diamond flower", "diamond flower", "diamond bouquet")
                        )

                        if not crafted_any:
                            print("These items cannot be crafted together.")
            else:
                print("Invalid inventory slots. Please enter numbers between 1 and 20.")
    elif whatdoyoudo == "pet": # pet - shows your pet
        if pet == "none":
            print("You don't have a pet.")
        else:
            print(f"Your pet is {pet}.")
    elif whatdoyoudo == "petrelease": #  petrelease - releases your pet unless you have a diamond flower active
        if pet == "none":
            print("You don't have a pet to release.")
        else:
            if diamondflowerstatus:
                print("you cannot release your pet while the diamond flower is active.")
            else:
                print(f"You release your pet, your pet was {pet}, do pickup to pick it up again.")
                justfound = pet
                pet = "none"
    elif whatdoyoudo == "exit": # exit - exits the game
        print("Thanks for playing!")  
        sys.exit()
    elif whatdoyoudo == "save": # save - saves the game
        savegame()
    elif whatdoyoudo == "load": # load - loads a save
        loadgame()
    elif whatdoyoudo == "reset diamond bouquet": # reset diamond bouquet - resets the diamond bouquet and makes the diamond flower unactive (debug command)
        if debug:
            diamondbouquetstatus = False
            diamondflowerstatus = False
            print("diamond bouquet reset and diamond flower is now unactive. (if you even had the diamond bouquet active)")
    elif whatdoyoudo == "reset diamond flower": # reset diamond flower - resets the diamond flower and makes it unactive (debug command)
        if debug:
            diamondflowerstatus = False
            print("diamond flower reset and is now unactive. (if you even had the diamond flower active)")
    elif whatdoyoudo == "reset house": # reset house - resets your house level to 0 and makes you have no house (debug command)
        if debug:
            houselevel = 0
            print("house reset, you now have no house. (if you even had a house)")
    elif whatdoyoudo == "reset pet": # reset pet - resets your pet to none and releases your pet if you have one (debug command)
        if debug:
            pet = "none"
            print("pet reset, you now have no pet. (if you even had a pet)")
    elif whatdoyoudo == "reset inventory": # reset inventory - resets your inventory and makes all inventory slots empty (debug command)
        if debug:
            for i in range(1, 21):
                globals()[f"inventoryslot{i}"] = "empty"
            print("inventory reset, all inventory slots are now empty.")
    elif whatdoyoudo == "reset all": # reset all - resets all progress, including pet, house level, inventory, and all other progress (debug command)
        if debug:
            pet = "none"
            houselevel = 0
            justfound = "nothing"
            item1name = ""
            item2name = ""
            item1 = None
            item2 = None
            diamondflowerstatus = False
            hatslot = "empty"
            shoesslot = "empty"
            diamondbouquetstatus = False
            for i in range(1, 21):
                globals()[f"inventoryslot{i}"] = "empty"
            print("all progress reset, pet, house level, inventory, and all other progress is now reset.")
    elif whatdoyoudo == "hat": # hat - shows your hat
        if hatslot == "empty":
            print("You are not wearing a hat.")
        else:
            print(f"You are wearing {hatslot} as a hat.")
    elif whatdoyoudo == "shoes": # shoes - shows your shoes
        if shoesslot == "empty":
            print("You are not wearing shoes.")
        else:
            print(f"You are wearing {shoesslot} as shoes.")
    elif whatdoyoudo.startswith("debug") and whatdoyoudo != "debug secretcode123goobergoble": # incorrect debug code - shows a message saying the debug code is incorrect
        print("Incorrect debug code. Please try again.")
    elif whatdoyoudo == "debug secretcode123goobergoble": # correct debug code - toggles debug mode
        if debug:
            debug = False
            print("Debug mode deactivated. Additional commands are now hidden.")
        else:
            debug = True
            print("Debug mode activated. Additional commands are now available.")
    elif whatdoyoudo == "lake": # lake - find a lake, but there is a small chance to find an axolotl instead of water
        if random.randint(1, 100) <= 5:
            print("You find a lake, but you see an axolotl just chilling in it")
            justfound = "a axolotl"
        else:
            print("You find a lake, type 'pickup' to collect some water.")
            justfound = "bottle of water"
    elif whatdoyoudo == "giveitem [name]": # gives a item to you no mater what (debug command)
        if debug:
            itemname = whatdoyoudo[11:]
            justfound = itemname
            if justfound == "nothing":
                print("There is nothing to pick up.")
            elif justfound == "evil ore":
                print("You pick up evil ore")
                print("what do you want to do? (type 'help' for a list of commands): ")
                time.sleep(2)
                print("you cant seem to type...")
                time.sleep(1)
                print("the evil ore fills you with darkness and you lose all your items and die")
                if diamondflowerstatus and pet != "none":
                    print("but your pet revives you because of the diamond flower")
                else:
                    sys.exit()
            else:
                for i in range(1, 21):
                    if globals().get(f"inventoryslot{i}") == "empty":
                        globals()[f"inventoryslot{i}"] = justfound
                        print(f"You pick up the {justfound}.")
                        print(f"it was placed in slot {i}")
                        justfound = "nothing"
                        break
                else:
                    print("Your inventory is full. You can't get this item.")
            
    else: # if the command is not recognized, show an error message
        print("Invalid command. Type 'help' for a list of commands.")
def mine(pickaxetype):
    global justfound
    if pickaxetype == "stone":
        minableitems = ["rock", "coal", "iron ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your stone pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "iron":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "sapphire ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your iron pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "diamond":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your diamond pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "gold":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "sapphire ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your gold pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "emerald":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your emerald pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "ruby":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "mythril ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your ruby pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "mythril":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "mythril ore", "adamantite ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your mythril pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "adamantite":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "mythril ore", "adamantite ore"]
        justfound = random.choice(minableitems)
        print(f"You mine with your adamantite pickaxe and find {justfound}! you can mine it by typing 'pickup'")

def loadgame():
    global pet, justfound
    load = input("Do you want to load a save? (yes/no): ")
    if load.lower() == "yes":
        loadwhere = input("Where is your save? (enter file path including the name and extension): ")
        try:
            with open(loadwhere, "r") as f:
                data = json.load(f)
                for i in range(1, 21):
                    globals()[f"inventoryslot{i}"] = data.get("inventory", ["empty"]*20)[i-1]
                pet = data.get("pet", "none")
                justfound = data.get("justfound", "nothing")
                houselevel = data.get("houselevel", 0)
                diamondflowerstatus = data.get("diamondflowerstatus", False)
                hatslot = data.get("hatslot", "empty")
                shoesslot = data.get("shoesslot", "empty")
                diamondbouquetstatus = data.get("diamondbouquetstatus", False)
                debug = data.get("debug", False)
            print("Progress loaded.")
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")

def savegame():
    global pet, justfound
    save = input("Do you want to save your progress? (yes/no): ")
    if save.lower() == "yes":
        where = input("Where do you want to save your progress? (enter file path including the name and extension): ")
        with open(where, "w") as f:
            json.dump({
                "inventory": [globals()[f"inventoryslot{i}"] for i in range(1, 21)],
                "pet": pet,
                "justfound": justfound,
                "houselevel": houselevel,
                "diamondflowerstatus": diamondflowerstatus,
                "hatslot": hatslot,
                "shoesslot": shoesslot,
                "diamondbouquetstatus": diamondbouquetstatus,
                "diamondflowerstatus": diamondflowerstatus,
                "debug": debug
            }, f)
        print("Progress saved.")

def crafting(firstitem, seconditem, resultitem):
    global item1, item2, item1name, item2name
    if ((item1name == firstitem and
    item2name == seconditem) or
    (item1name == seconditem and
    item2name == firstitem)):
        print(f"You crafted a {resultitem}!")
        globals()[f"inventoryslot{item1}"] = resultitem
        globals()[f"inventoryslot{item2}"] = "empty"
        print(f"The crafted item has been placed in slot {item1}.")
        return True
    return False

loadgame()
while True:
    main()
