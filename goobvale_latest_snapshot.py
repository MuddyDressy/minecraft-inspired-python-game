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
armorslot = "empty"
diamondbouquetstatus = False
debug = False
money = 0
draw = "notdrawn"
GoblinKingAlive = True
items = {
    ## Basic Items

    "rock": 0.1,
    "flower": 0.1,
    "wood": 0.2,
    "sand": 0.1,
    "glass": 1.3,
    "boulder": 0.3,

    ## Gems and Treasure Chain

    "gem": 1,
    "big gem": 2.2,
    "treasure box": 11.5,
    # diamond ore used to be here but i dont want duplicates so its only in the mining area of the items dictinary now

    ## Pickaxes

    "stone pickaxe": 0.5,
    "iron pickaxe": 1.4,
    "gold pickaxe": 5.4,
    "diamond pickaxe": 10.5,
    "emerald pickaxe": 15.5,
    "ruby pickaxe": 20.6,
    "mythril pickaxe": 50.8,
    "adamantite pickaxe": 76,

    ## Swords

    "stone sword": 0.5,
    "iron sword": 1.4,
    "gold sword": 5.4,
    "diamond sword": 10.5,
    "emerald sword": 15.5,
    "ruby sword": 20.6,
    "mythril sword": 50.8,
    "adamantite sword": 76,

    ## Pets

    # pets are unbuyable and unsellable (yeah... i know you think the pets should be buyable and sellable at like $1000 but i think that would break the economy of the game so thats why i put them in a diffrent list)

    ## Pet Related Items

    "bouquet": 0.4,
    "diamond bouquet": 21.6,
    "diamond flower": 10.6,
    "glasses": 2,

    ## Other
    "magic wand": 1.4,
    "bottle of water": 0.1,
    "paper": 5,
    "crafting recipe book": 15.7,
    "Goblin Key": 20,
    "Goblin Crown": 3000,

    ## Minerals/Ores

    "coal": 1,
    "iron ore": 3,
    "gold ore": 7.5,
    "diamond ore": 10,
    "emerald ore": 15,
    "ruby ore": 20,
    "sapphire ore": 15,
    "evil ore": 30,
    "mythril ore": 50,
    "adamantite ore": 75
}

pets = [
    "a rabbit",
    "a magic rabbit",
    "a cool rabbit",
    "a cool magic rabbit",
    "mystics cat",
    "a axolotl"
]

armors = {
    "iron chestplate": 7,
    "diamond chestplate": 12,
    "gold chestplate": 6,
    "emerald chestplate": 15,
    "ruby chestplate": 17,
    "mythril chestplate": 20,
    "adamantite chestplate": 25
}
def main():
    global justfound, pet, houselevel, item1, item2, item1name, item2name, diamondflowerstatus, hatslot, armorslot, diamondbouquetstatus, debug, money, draw, GoblinKingAlive
    whatdoyoudo = input("what do you want to do? (type 'help' for a list of commands): ")
    if whatdoyoudo == "help": # help command, shows a list of commands
        print("help - shows this message")
        print("inventory [1-20] - shows whats in that specific inventory slot (put no number to see whats in all inventory slots)")
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
            print("giveitem [name] - gives you an item")
            print("givemoney [amount] - gives you money")
            print("draw - lets you draw on a piece of paper")
            print("seedrawing - shows your drawing if you have drawn on the paper")
            print("fight [enemy name] - fights an enemy (you can only fight enemies that are in the fight function, and you have to type the name exactly right)")
        print("hat - shows your hat")
        print("armor - shows your armor")
        print("money - shows your money")
        print("lake - find a lake")
        print("shop - buy and sell items")
        print("value [item name] - shows the value of an item, only works if the item is in the shop")
        print("shopitems - shows a list of items in the shop")
        print("wander - wander around, maybe you'll find something")
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
                if houselevel > 0:
                    print("you already have a house, you dont need to use the wood to make another one.")
                else:
                    print("You use the wood to make a house.")
                    justfound = "nothing"
                    houselevel = 1
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
                print("you cannot use a mineral, it can only be crafted with other items or sold for money.")
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
            elif item == "bottle of water":
                print("You drink the bottle of water and feel refreshed.")
                globals()[f"inventoryslot{slot}"] = "empty"
            elif item == "paper":
                if draw != "notdrawn":
                    drawornot = input("you've already drawn on the paper, do you want to overwrite your drawing or look at it? (overwrite/look): ")
                    if drawornot == "overwrite":
                        draw = "notdrawn"
                    elif drawornot == "look":
                        for row in draw:
                            print(" ".join("▢" if cell == " " else cell for cell in row))
                elif draw == "notdrawn":
                    print("you wanna draw on the paper, so lets see what you can do...")
                    draw()
            elif item == "crafting recipe book":
                print("the crafting recipe book has the following crafting recipes in it:")
                print("wood + gem = magic wand")
                print("wood + rock = stone pickaxe or stone sword (choose one when crafting)")
                print("wood + iron ore = iron pickaxe or iron sword (choose one when crafting)")
                print("wood + diamond ore = diamond pickaxe or diamond sword (choose one when crafting)")
                print("wood + gold ore = gold pickaxe or gold sword (choose one when crafting)")
                print("wood + emerald ore = emerald pickaxe or emerald sword (choose one when crafting)")
                print("wood + ruby ore = ruby pickaxe or ruby sword (choose one when crafting)")
                print("wood + mythril ore = mythril pickaxe or mythril sword (choose one when crafting)")
                print("wood + adamantite ore = adamantite pickaxe or adamantite sword (choose one when crafting)")
                print("a rabbit + gem = a magic rabbit")
                print("flower + flower = bouquet")
                print("rock + rock = boulder")
                print("gem + gem = big gem")
                print("wood + glass = glasses")
                print("a rabbit + glasses = a cool rabbit")
                print("a magic rabbit + glasses = a cool magic rabbit")
                print("coal + sand = glass")
                print("a cool rabbit + gem = a cool magic rabbit")
                print("diamond ore + flower = diamond flower")
                print("diamond flower + diamond flower = diamond bouquet")
                print("wood + bottle of water = paper")
                print("wood + paper = crafting recipe book")
            elif item == "stone sword" or item == "iron sword" or item == "gold sword" or item == "diamond sword" or item == "emerald sword" or item == "ruby sword" or item == "mythril sword":
                print("you swing around your sword thinking about how cool it is.")
            elif item == "adamantite sword":
                print("you swing around your adamantite sword, it feels very powerful and you feel like you could defeat any enemy with it.")
            elif item == "Goblin Key":
                if GoblinKingAlive:
                    print("You use the Goblin Key to open a key to the Goblin King's Domain...")
                    time.sleep(2)
                    print("Goblin King: You are NOT a Goblin, You cannot stay here!")
                    time.sleep(0.5)
                    print("Goblin King: If you want to come out alive, you must defeat me in a battle!")
                    time.sleep(0.5)
                    print("Goblin King: But First you will fight my minions!")
                    time.sleep(0.5)
                    print("Fight Initiates!")
                    time.sleep(0.5)
                    fight("Goblin Group", 60, 7, "Dog Pile", 10, "Multi-Stab", 13, "Coin Pile Dump", 90, "None")
                    time.sleep(0.5)
                    print("Goblin King: Huh, not bad for a non-goblin, but you still have to fight me if you want to stay here!")
                    time.sleep(0.5)
                    fight("Goblin King", 150, 15, "Sword Slash", 20, "Ground Pound", 25, "Summon Minions", 200, "Goblin Crown")
                    time.sleep(0.5)
                    print("Goblin King: AHHH NOOO *SCREAMING IN PAIN* bleh.")
                    time.sleep(0.5)
                    print("You left the Goblin King's Domain with the Goblin Crown, which is worth a lot of money!")
                    globals()[f"inventoryslot{slot}"] = "empty"
                else:
                    print("The Goblin King is already dead, Key has no use now.")
            elif item == "Goblin Crown":
                print("You put on the Goblin Crown and feel an immense power coursing through your veins. You have become the new Goblin King!")
                hatslot = "Goblin Crown"
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
            if random.randint(1, 100) <= 10:
                print("you find a tree, but it was wisdom tree")
                givemoney = input("do you want to give money to the wisdom tree to get wisdom? (yes/no): ")
                if givemoney == "yes":
                    if money >= 10:
                        money -= 10
                        print("you give the wisdom tree 10 money")
                        print("his wisdom is...")
                        wisdom = random.choice(["you cant win without losing first", "the journey is more important than the destination", "dont cry over spilled milk", "a rolling stone gathers no moss", "actions speak louder than words", "you are what you eat", "the early bird catches the worm", "you miss 100% of the shots you dont take", "when one door closes another opens", "fortune favors the bold", "the only way to get to your dreams is to work hard for them", "you can do anything you set your mind to", "the best things in life are free", "you cant make a cake and eat it too", "a picture is worth a thousand words", "when the going gets tough the tough get going", "two wrongs dont make a right", "the grass is always greener on the other side", "you cant judge a book by its cover", "if it aint broke dont fix it", "beauty is in the eye of the beholder", "losing doesnt mean you are a failure, it just means your learning", "the key to success is to never give up", "the best way to predict the future is to create it", "i forgot what he was going to say, so ill just give you the money back", "the secret to getting job is to get a job that rewards you for what you love doing", "the secret to happiness is to be happy with what you have already acomplished"])
                        print(wisdom)
                        if wisdom == "i forgot what he was going to say, so ill just give you the money back":
                            money += 10
                    else:
                        print("you dont have enough money to give the wisdom tree, you need at least 10 money to get wisdom from the wisdom tree.")
                else:
                    print("you don't give the wisdom tree any money and it ignores you.")
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
            print("You pick up the evil ore")
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
                            crafting("wood", "gem", "magic wand", "none") or
                            crafting("wood", "rock", "stone pickaxe", "stone sword") or
                            crafting("wood", "iron ore", "iron pickaxe", "iron sword") or
                            crafting("wood", "diamond ore", "diamond pickaxe", "diamond sword") or
                            crafting("wood", "gold ore", "gold pickaxe", "gold sword") or
                            crafting("wood", "emerald ore", "emerald pickaxe", "emerald sword") or
                            crafting("wood", "ruby ore", "ruby pickaxe", "ruby sword") or
                            crafting("wood", "mythril ore", "mythril pickaxe", "mythril sword") or
                            crafting("wood", "adamantite ore", "adamantite pickaxe", "adamantite sword") or
                            crafting("a rabbit", "gem", "a magic rabbit", "none") or
                            crafting("flower", "flower", "bouquet", "none") or
                            crafting("rock", "rock", "boulder", "none") or
                            crafting("gem", "gem", "big gem", "none") or
                            crafting("wood", "glass", "glasses", "none") or
                            crafting("a rabbit", "glasses", "a cool rabbit", "none") or
                            crafting("a magic rabbit", "glasses", "a cool magic rabbit", "none") or
                            crafting("coal", "sand", "glass", "none") or
                            crafting("a cool rabbit", "gem", "a cool magic rabbit", "none") or
                            crafting("diamond ore", "flower", "diamond flower", "none") or
                            crafting("diamond flower", "diamond flower", "diamond bouquet", "none") or
                            crafting("wood", "bottle of water", "paper", "none") or
                            crafting("wood", "paper", "crafting recipe book", "none") or
                            crafting("iron ore", "iron ore", "iron chestplate", "none") or
                            crafting("diamond ore", "diamond ore", "diamond chestplate", "none") or
                            crafting("gold ore", "gold ore", "gold chestplate", "none") or
                            crafting("emerald ore", "emerald ore", "emerald chestplate", "none") or
                            crafting("ruby ore", "ruby ore", "ruby chestplate", "none") or
                            crafting("mythril ore", "mythril ore", "mythril chestplate", "none") or
                            crafting("adamantite ore", "adamantite ore", "adamantite chestplate", "none")
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
        save()
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
            armorslot = "empty"
            diamondbouquetstatus = False
            for i in range(1, 21):
                globals()[f"inventoryslot{i}"] = "empty"
            print("all progress reset, pet, house level, inventory, and all other progress is now reset.")
    elif whatdoyoudo == "hat": # hat - shows your hat
        if hatslot == "empty":
            print("You are not wearing a hat.")
        else:
            print(f"You are wearing {hatslot} as a hat.")
    elif whatdoyoudo == "armor": # armor - shows your armor
        if armorslot == "empty":
            print("You are not wearing armor.")
        else:
            print(f"You are wearing {armorslot} as armor.")
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
    elif whatdoyoudo.startswith("giveitem "): # giveitem [name] - gives a item to you no mater what (debug command)
        if debug:
            itemname = whatdoyoudo[9:]
            justfound = itemname
            if justfound == "nothing":
                print("There is nothing to pick up.")
            elif justfound == "evil ore":
                print("You get evil ore")
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
                        print(f"You get {justfound}.")
                        print(f"it was placed in slot {i}")
                        justfound = "nothing"
                        break
                else:
                    print("Your inventory is full. You can't get this item.")
    elif whatdoyoudo == "money": # money - shows your money
        print(f"You have {round(money, 2)} money.")
    elif whatdoyoudo == "inventory": # inventory - shows all your inventory slots and what is in them
        for i in range(1, 21):
            print(f"Slot {i}: {globals().get(f'inventoryslot{i}')}")
    elif whatdoyoudo == "shop": # shop - buy and sell items
        buyorsell = input("do you want to buy or sell items? (buy/sell): ")
        if buyorsell == "buy":
            itemtobuy = input("What would you like to buy? (type the name of the item you want to buy, or type 'exit' to exit the shop): ")
            if itemtobuy == "exit":
                print("Thanks for visiting the shop!")
            elif itemtobuy in items:
                if money >= items[itemtobuy]:
                    money -= items[itemtobuy]
                    justfound = itemtobuy
                    print(f"You bought {itemtobuy} for {items[itemtobuy]} money. type 'pickup' to pick it up.")
                else:
                    print(f"You don't have enough money to buy this item. the price of the item is {items[itemtobuy]} money.")
            else:
                print("This item is not available for purchase, if it is a pet, pets are not allowed to be sold or bought in the shop.")
        elif buyorsell == "sell":
            itemtosell = input("type the slot that the item you want to sell is in (type a number between 1 and 20, or type 'exit' to exit the shop): ")
            if itemtosell == "exit":
                print("Thanks for visiting the shop!")
            elif itemtosell.isdigit() and 1 <= int(itemtosell) <= 20:
                itemtosell = int(itemtosell)
                if globals().get(f"inventoryslot{itemtosell}") == "empty":
                    print("That slot is empty. you have nothing to sell in that slot.")
                else:
                    itemsellname = globals().get(f"inventoryslot{itemtosell}")
                    if itemsellname in items:
                        money += items[itemsellname]
                        print(f"You sold {itemsellname} for {items[itemsellname]} money.")
                        globals()[f"inventoryslot{itemtosell}"] = "empty"
                    else:
                        print("This item cannot be sold as it is not in the shop's inventory, if it is a pet, pets are not allowed to be sold or bought in the shop.")
            else:
                print("Invalid inventory slot. Please enter a number between 1 and 20, or type 'exit' to exit the shop.")
    elif whatdoyoudo == "givemoney [amount]": # give money to the player
        if debug:
            amount = input("How much money do you want to give? (enter a number): ")
            if amount.isdigit():
                amount = int(amount)
                money += amount
                print(f"You received {amount} money.")
            else:
                print("Invalid amount. Please enter a valid number.")
    elif whatdoyoudo.startswith("runcode "): # runcode - runs code that is only for testing and debugging purposes, it is not meant to be used by players and can break the game if used incorrectly
        if debug:
            code = whatdoyoudo[8:]
            try:
                exec(code)
                print("Code executed successfully:")
                print(code)
            except Exception as e:
                print(f"An error occurred while executing the code: {e}")
    elif whatdoyoudo.startswith("value "): # value [item name] - shows the value of an item, only works if the item is in the shop
        itemname = whatdoyoudo[6:]
        if itemname in items:
            print(f"The value of {itemname} is {items[itemname]} money.")
        else:
            print("This item is not in the shop, so its value cannot be determined.")
    elif whatdoyoudo == "draw": # draw - lets you draw on a piece of paper (debug command)
        if debug:
            print("lets see what you can draw...")
            draw()
    elif whatdoyoudo == "seedrawing": # seedrawing - shows your drawing if you have drawn on the paper (debug command)
        if debug:
            print("your drawing is:")
            for row in draw:
                print(" ".join("▢" if cell == " " else cell for cell in row))
    elif whatdoyoudo == "shopitems": # shopitems - shows all the items that are in the shop
        print("the shop has the following items for sale:")
        for item, price in items.items():
            print(f"{item}: {price} money")
    elif whatdoyoudo == "wander": # wander - wander around, maybe you'll find something
        print("you wander around")
        event = random.randint(1, 100)
        if event <= 40:
            print("nothing intresting happens.")
        elif event >= 90:
            print("you find some money on the ground!")
            moneyfound = random.uniform(0.5, 5.0)
            money += moneyfound
            print(f"You Got {round(moneyfound, 2)} money.")
        elif event <= 60:
            print("You find a rock on the ground! ('pickup' to pick it up)")
            justfound = "rock"
        elif event <= 80:
            print("YOU FOUND A UNTAMED WOLF! Fight Initiates!")
            fight("Wolf", 20, 5, "Bite", 6, "Charge", 8, "Jump Attack", 10, "None")
    elif whatdoyoudo.startswith("fight"): # fight - initiates a fight with a random enemy (debug command)
        if debug:
            enemy = whatdoyoudo[6:]
            if enemy == "random" or enemy == "":
                enemy = random.choice(["Wolf", "Player", "Goblin"])
            elif enemy == "Wolf".lower():
                fight("Wolf", 20, 5, "Bite", 6, "Charge", 8, "Jump Attack", 10, "None")
            elif enemy == "Player".lower():
                fight("Player", 30, 6, "Punch", 8, "Kick", 15, "Uppercut", 0, "None")
            elif enemy == "Goblin".lower():
                fight("Goblin", 25, 4, "Slam", 6, "Stab", 8, "Coin Throw", 30, "Goblin Key")
            elif enemy == "Goblin King".lower():
                fight("Goblin King", 150, 15, "Sword Slash", 20, "Ground Pound", 25, "Summon Minions", 200, "Goblin Crown")
            elif enemy == "Goblin Group".lower():
                fight("Goblin Group", 60, 6, "Dog Pile", 9, "Multi-Stab", 12, "Coin Pile Dump", 90, "None")
            else:
                print(f"{enemy} not found.")
    else: # if the command is not recognized, show an error message
        print("Invalid command. Type 'help' for a list of commands.")

def mine(pickaxetype):
    global justfound
    if pickaxetype == "stone":
        minableitems = ["rock", "coal", "iron ore"]
        justfound = random.choice(minableitems)
        if pet == "rabbit" and justfound == "rock":
            mine(pickaxetype="stone")
        else:
            print(f"You mine with your stone pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "iron":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "sapphire ore"]
        justfound = random.choice(minableitems)
        if pet == "rabbit" and justfound == "rock":
            mine(pickaxetype="iron")
        else:
            print(f"You mine with your iron pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "diamond":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "goblin instead"]
        justfound = random.choice(minableitems)
        if justfound == "goblin instead":
            print(f"You mine with your {pickaxetype} pickaxe but instead of finding a mineral, you find a goblin! Fight Initiates!")
            fight("Goblin", 25, 4, "Slam", 6, "Stab", 8, "Coin Throw", 30, "Goblin Key")
        else:
            if pet == "rabbit" and justfound == "rock":
                mine(pickaxetype="diamond")
            else:
                print(f"You mine with your diamond pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "gold":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "sapphire ore"]
        justfound = random.choice(minableitems)
        if pet == "rabbit" and justfound == "rock":
            mine(pickaxetype="gold")
        else:
            print(f"You mine with your gold pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "emerald":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "goblin instead"]
        justfound = random.choice(minableitems)
        if justfound == "goblin instead":
            print(f"You mine with your {pickaxetype} pickaxe but instead of finding a mineral, you find a goblin! Fight Initiates!")
            fight("Goblin", 25, 4, "Slam", 6, "Stab", 8, "Coin Throw", 30, "Goblin Key")
        else:
            if pet == "rabbit" and justfound == "rock":
                mine(pickaxetype="emerald")
            else:
                print(f"You mine with your emerald pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "ruby":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "mythril ore", "goblin instead"]
        justfound = random.choice(minableitems)
        if justfound == "goblin instead":
            print(f"You mine with your {pickaxetype} pickaxe but instead of finding a mineral, you find a goblin! Fight Initiates!")
            fight("Goblin", 25, 4, "Slam", 6, "Stab", 8, "Coin Throw", 30, "Goblin Key")
        else:
            if pet == "rabbit" and justfound == "rock":
                mine(pickaxetype="ruby")
            else:
                print(f"You mine with your ruby pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "mythril":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "mythril ore", "adamantite ore", "goblin instead"]
        justfound = random.choice(minableitems)
        if justfound == "goblin instead":
            print(f"You mine with your {pickaxetype} pickaxe but instead of finding a mineral, you find a goblin! Fight Initiates!")
            fight("Goblin", 25, 4, "Slam", 6, "Stab", 8, "Coin Throw", 30, "Goblin Key")
        else:
            if pet == "rabbit" and justfound == "rock":
                mine(pickaxetype="mythril")
            else:
                print(f"You mine with your mythril pickaxe and find {justfound}! you can mine it by typing 'pickup'")
    elif pickaxetype == "adamantite":
        minableitems = ["rock", "coal", "iron ore", "gold ore", "diamond ore", "emerald ore", "ruby ore", "sapphire ore", "evil ore", "mythril ore", "adamantite ore", "goblin instead"]
        justfound = random.choice(minableitems)
        if justfound == "goblin instead":
            print(f"You mine with your {pickaxetype} pickaxe but instead of finding a mineral, you find a goblin! Fight Initiates!")
            fight("Goblin", 25, 5, "Slam", 6, "Stab", 8, "Coin Throw", 30, "Goblin Key")
        else:
            if pet == "rabbit" and justfound == "rock":
                mine(pickaxetype="adamantite")
            else:
                print(f"You mine with your adamantite pickaxe and find {justfound}! you can mine it by typing 'pickup'")

def loadgame():
    global pet, justfound
    load = input("Do you want to load a save? (yes/no): ")
    if load.lower() == "yes":
        loadwhere = input("Where is your save? (enter file path including the name and extension): ")
        try:
            with open(loadwhere, "r") as f:
                data = json.load(f)
                inv = data.get("inventory", ["empty"]*20)
                for i in range(20):
                    globals()[f"inventoryslot{i+1}"] = inv[i] if i < len(inv) else "empty"
                pet = data.get("pet", "none")
                justfound = data.get("justfound", "nothing")
                houselevel = data.get("houselevel", 0)
                diamondflowerstatus = data.get("diamondflowerstatus", False)
                hatslot = data.get("hatslot", "empty")
                armorslot = data.get("armorslot", "empty")
                diamondbouquetstatus = data.get("diamondbouquetstatus", False)
                debug = data.get("debug", False)
                money = data.get("money", 0)
                GoblinKingAlive = data.get("GoblinKingAlive", True)
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
                "armorslot": armorslot,
                "diamondbouquetstatus": diamondbouquetstatus,
                "diamondflowerstatus": diamondflowerstatus,
                "debug": debug,
                "money": money,
                "GoblinKingAlive": GoblinKingAlive
            }, f)
        print("Progress saved.")

def crafting(firstitem, seconditem, resultitem, resultitem2):
    finalresultitem = "none"
    global item1, item2, item1name, item2name
    if ((item1name == firstitem and
    item2name == seconditem) or
    (item1name == seconditem and
    item2name == firstitem)):
        if resultitem2 == "none":
            finalresultitem = resultitem
        else:
            while finalresultitem not in [resultitem, resultitem2]:
                finalresultitem = input(f"would you like to craft this item into {resultitem2} or {resultitem}? (type the name of the item you want to craft): ")
                if finalresultitem != resultitem and finalresultitem != resultitem2:
                    print("Invalid choice. Please type the name of the item you want to craft.")
        print(f"You crafted a {finalresultitem}!")
        globals()[f"inventoryslot{item1}"] = finalresultitem
        globals()[f"inventoryslot{item2}"] = "empty"
        print(f"The crafted item has been placed in slot {item1}.")
        return True
    return False

def draw():
    global draw
    canvassize = input("type a width and height for your drawing canvas between 1 and 10 (for example, '5 5' for a 5 by 5 canvas): ")
    canvaswidth = canvassize.split(" ")[0]
    canvasheight = canvassize.split(" ")[1]
    if canvaswidth.isdigit() and canvasheight.isdigit():
        canvaswidth = int(canvaswidth)
        canvasheight = int(canvasheight)
        if 1 <= canvaswidth <= 10 and 1 <= canvasheight <= 10:
            canvas = [[" " for _ in range(canvaswidth)] for _ in range(canvasheight)]
            for row in canvas:
                print(" ".join("▢" if cell == " " else cell for cell in row))
        else:
            print("Width and height must be between 1 and 10.")
    else:
        print("Invalid input. Please enter numbers only.")
    draw = input("type 'draw [x] [y]' to draw on the canvas (type erase instead of draw to erase), where x is the width and y is the height from the top left corner (for example, 'draw 2 3' to draw on the 2nd column and 3rd row), type 'done' to finish: ")
    while draw != "done":
        if draw.startswith("draw ") or draw == "done":
            parts = draw.split(" ")
            if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
                x = int(parts[1]) - 1
                y = int(parts[2]) - 1
                if 0 <= x < canvaswidth and 0 <= y < canvasheight:
                    canvas[y][x] = "▨"
                    for row in canvas:
                        print(" ".join("▢" if cell == " " else cell for cell in row))
                else:
                    print("Coordinates out of bounds. Please enter values within the canvas size.")
            else:
                print("Invalid command format. Use 'draw [x] [y]' with valid numbers.")
        elif draw.startswith("erase ") or draw == "done":
            parts = draw.split(" ")
            if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
                x = int(parts[1]) - 1
                y = int(parts[2]) - 1
                if 0 <= x < canvaswidth and 0 <= y < canvasheight:
                    canvas[y][x] = "▢"
                    for row in canvas:
                        print(" ".join("▢" if cell == " " else cell for cell in row))
                else:
                    print("Coordinates out of bounds. Please enter values within the canvas size.")
            else:
                print("Invalid command format. Use 'erase [x] [y]' with valid numbers.")
        else:
            print("Invalid command. Type 'draw [x] [y]' to draw or 'done' to finish.")
        draw = input("type 'draw [x] [y]' to draw on the canvas (type erase instead of draw to erase), where x is the width and y is the height from the top left corner (for example, 'draw 2 3' to draw on the 2nd column and 3rd row), type 'done' to finish: ")
    draw = canvas

def fight(enemyname, enemyhealth, enemybasicattackdamage, enemybasicattackname, enemystrongattackdamage, enemystrongattackname, enemyultimateattackdamage, enemyultimateattackname, enemymoneydrop, extraitemdrop):
    global money
    turn = "player"
    print(f"You are fighting a {enemyname}!")
    playerhealth = 30
    playerbasicattackdamage = 6
    playerbasicattackname = "Punch"
    playerstrongattackdamage = 8
    playerstrongattackname = "Kick"
    playerultimateattackdamage = 10
    playerultimateattackname = "Headbutt"
    ememyultimatecooldown = 0
    playerultimatecooldown = 0
    petultimatecooldown = 0
    baseenemyhealth = enemyhealth
    if armor in armors:
        playerhealth += armors[armor]
    enemyconfused = False
    while enemyhealth > 0:
        print(f"you currently have {playerhealth} health")
        print(f"the {enemyname} currently has {enemyhealth} health")
        if turn == "player":
            action = input("do you want to use your basic attack, strong attack, ultimate attack or talk to the enemy? (basic/strong/ultimate/talk or use [item slot] to use an item and exit to leave the game): ")
            time.sleep(0.5)
            if action == "basic":
                print(f"You use {playerbasicattackname} and deal {playerbasicattackdamage} damage!")
                enemyhealth -= playerbasicattackdamage
                turn = "enemy"
                playerultimatecooldown = max(0, playerultimatecooldown - 1)
            elif action == "strong":
                print(f"You use {playerstrongattackname} and deal {playerstrongattackdamage} damage!")
                enemyhealth -= playerstrongattackdamage
                turn = "enemy"
                playerultimatecooldown = max(0, playerultimatecooldown - 1)
            elif action == "ultimate":
                if playerultimatecooldown > 0:
                    print(f"Your ultimate attack is on cooldown for {playerultimatecooldown} more turns.")
                else:
                    print(f"You use {playerultimateattackname} and deal {playerultimateattackdamage} damage!")
                    enemyhealth -= playerultimateattackdamage
                    playerultimatecooldown = 3
                    turn = "enemy"
            elif action == "exit":
                print("Thanks for playing! (saving will not save your fight progress, only your overall game progress, so if you load your save after exiting, you will have to get the fight again but you will keep all your items, pets, house level, and other progress)")
                save()
                sys.exit()
            elif action == "talk":
                print(f"You try to talk to the {enemyname}")
                if enemyname == "Goblin":
                    print("The Goblin takes it as a threat and says 'You think you can talk your way out of this? YOU'RE GONNA DIE KID' and continues to fight you.")
                elif enemyname == "Goblin King":
                    print("The Goblin King thinks your stupid and says 'This is a fight to the death, only 1 comes out alive and your gonna be the one that dies, you cant talk your way out of a fight with the Goblin King' and continues to fight you.")
                elif enemyname == "Goblin Group":
                    print("You talk ask them a very controversial question, they come out with diffrent answers and fight each other, hurting other goblins.")
                    enemyhealth -= 7
                elif enemyname == "Wolf":
                    print("The Wolf looks at you realizing you are not a threat, you tame the wolf (use 'pickup' to pick it up then 'use [item slot]' to make it your pet).")
                    justfound = "A Tamed Wolf"
                else:
                    print(f"You try to talk to the {enemyname}, but it just has a identity crisis then goes back to fighting you like normal.")
            elif action.startswith("use "):
                if action[4:].isdigit() and 1 <= int(action[4:]) <= 20:
                    itemslot = int(action[4:])
                    itemname = globals().get(f"inventoryslot{itemslot}")
                    if itemname == "empty":
                        print("That slot is empty. you have no item to use in that slot.")
                    else:
                        print(f"You use the {itemname} in slot {itemslot}.")
                        if itemname == "stone sword":
                            print("The stone sword deals 8 damage!")
                            enemyhealth -= 8
                            turn = "enemy"
                        elif itemname == "iron sword":
                            print("The iron sword deals 10 damage!")
                            enemyhealth -= 10
                            turn = "enemy"
                        elif itemname == "diamond sword":
                            print("The diamond sword deals 12 damage!")
                            enemyhealth -= 12
                            turn = "enemy"
                        elif itemname == "magic wand":
                            print("The magic wand confuses the enemy and the enemy will now not take the next turn.")
                            enemyconfused = True
                            turn = "enemy"
                        elif itemname == "gold sword":
                            print("The gold sword deals 9 damage!")
                            enemyhealth -= 9
                            turn = "enemy"
                        elif itemname == "emerald sword":
                            print("The emerald sword deals 11 damage!")
                            enemyhealth -= 11
                            turn = "enemy"
                        elif itemname == "ruby sword":
                            print("The ruby sword deals 14 damage!")
                            enemyhealth -= 13
                            turn = "enemy"
                        elif itemname == "mythril sword":
                            print("The mythril sword deals 16 damage!")
                            enemyhealth -= 14
                            turn = "enemy"
                        elif itemname == "adamantite sword":
                            print("The adamantite sword deals 18 damage!")
                            enemyhealth -= 15
                            turn = "enemy"
                        elif itemname == "A Tamed Wolf" or int(action[4:]) == "pet" and pet == "A Tamed Wolf":
                            print("You send your tamed wolf to attack the enemy, it deals 7 damage!")
                            if petultimatecooldown > 0:
                                petaction = random.choice(["basic", "strong"])
                            else:
                                petaction = random.choice(["basic", "strong", "ultimate"])
                            if enemyaction == "basic":
                                print(f"The Tamed Wolf uses Bite and deals 5 damage!")
                                enemyhealth -= 5
                                turn = "enemy"
                                enemyultimatecooldown = max(0, playerultimatecooldown - 1)
                            elif enemyaction == "strong":
                                print(f"The Tamed Wolf uses Charge and deals 6 damage!")
                                enemyhealth -= 6
                                turn = "enemy"
                            elif enemyaction == "ultimate":
                                print(f"The Tamed Wolf uses Jump Attack and deals 10 damage!")
                                enemyhealth -= 10
                                turn = "enemy"
                                enemyultimatecooldown = 3
                            turn = "enemy"
                        else:
                            print("This item cannot be used in battle.")
            else:
                print("Invalid action. Please choose 'basic', 'strong', or 'ultimate' or 'use [item slot]'.")
        elif turn == "enemy":
            if ememyultimatecooldown > 0:
                enemyaction = random.choice(["basic", "strong"])
            else:
                enemyaction = random.choice(["basic", "strong", "ultimate"])
            time.sleep(0.5)
            if enemyconfused:
                print(f"The {enemyname} is confused and does not take a turn!")
                enemyconfused = False
                turn = "player"
            else:
                if enemyaction == "basic":
                    print(f"The {enemyname} uses {enemybasicattackname} and deals {enemybasicattackdamage} damage!")
                    playerhealth -= enemybasicattackdamage
                    turn = "player"
                    enemyultimatecooldown = max(0, playerultimatecooldown - 1)
                elif enemyaction == "strong":
                    print(f"The {enemyname} uses {enemystrongattackname} and deals {enemystrongattackdamage} damage!")
                    playerhealth -= enemystrongattackdamage
                    turn = "player"
                elif enemyaction == "ultimate":
                    print(f"The {enemyname} uses {enemyultimateattackname} and deals {enemyultimateattackdamage} damage!")
                    playerhealth -= enemyultimateattackdamage
                    turn = "player"
                    enemyultimatecooldown = 3
        if playerhealth <= 0:
            print("You have been defeated!")
            if diamondflowerstatus and pet != "none":
                print("your pet cannot revive you for balancing reasons")
                playerhealth = 30
            else:
                print("zzzz... oh that death was just a dream, you wake up back in the battle arena")
                turn = "player"
                playerhealth = 30
                enemyhealth = baseenemyhealth
                playerultimatecooldown = 0
                ememyultimatecooldown = 0
                petultimatecooldown = 0
        elif enemyhealth <= 0:
            print(f"You have defeated the {enemyname}!")
            if enemymoneydrop == 0:
                print("it didnt drop any money...")
            else:
                print(f"it dropped {enemymoneydrop} money! (for some reason...)")
            if extraitemdrop != "None":
                print(f"it also dropped a {extraitemdrop}! type 'pickup' to pick it up.")
                justfound = extraitemdrop
            money += enemymoneydrop          
                    
loadgame()
while True:
    main()
