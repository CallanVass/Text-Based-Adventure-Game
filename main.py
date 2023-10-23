from classes import *
import time
import random
import subprocess

cell_door_open = False
prisoners_free = False
servant_killed = False
servant_unconscious = False
tresury_entered = False
tunnel_door_opened = False
dig_counter = 1
tunnel_travelled_down = False
ominous_spirit_stare_counter = 1
asked_riddle = False
bowed_before_ominous_spirit = False
tunnel_prompt_list_1_asked = False
main_character_is_vampire = False
treasury_guard_dead = False
armoury_guards_dead = False
armoury_entered = False

# main_character.check_stats()
notebook = Notebook()
main_character = Character("Argus")

#NOTEBOOK FUNCTION
def append_arm():
    notebook = Notebook()
    notebook.read_notebook()
    notebook.write_notebook()
    return

#OPTIONS FUNCTION
def options(option_list, room):
    room.get_name()
    for index, option in enumerate(option_list):
        print(f"Option {index + 1}: {option}")
    return

#DISPLAY CHARACTER STATS
def display_stats():
    print(main_character.check_stats())
    print(prompt)
    return

#ADD NEW PROMPT/REMOVE OLD PROMPT
def remove_last_option(prompt_list, new_prompt):
    prompt_list.pop()
    prompt_list.append(new_prompt)

#CHANCE FUNCTION
def chance_of_success(percentage):
        random_nums = [random.randint(1, 10) for _ in range(percentage)]
        if percentage == 1:
            if 1 in random_nums:
                return "Your attempt fails!"
            else:
                return "Your attempt succeeds!"
        if percentage == 2:
            if any(value in random_nums for value in (1, 2)):
                return "Your attempt fails!"
            else:
                return "Your attempt succeeds!"
        if percentage == 3:
            if any(value in random_nums for value in (1, 2, 3)):
                return "Your attempt fails!"
            else:
                return "Your attempt succeeds!"
        if percentage >= 4:
            print("Callan, you turd, that's a stupidly high percentage. Change it right now.")

def quick_time_event(character, time_limit, health_lost, room):
        enemy_killed = False
        quick_time_prompt_list = ["Drain them dry!",
                                  "Knock them unconscious!"]
        while enemy_killed == False:
            start = time.time()
            quick_user_input = input(f"Quickly press Enter to fight back: ")
            end = time.time()
            time_passed = end - start
            if quick_user_input == "" and time_passed < time_limit:
                print("What would you like to do?")
                options(quick_time_prompt_list, room)
                quick_user_input_1 = input(">>> ")
                while quick_user_input_1 == "1":
                    print("You feed, throwing the body aside like a wet blanket!")
                    main_character.add_blood_glut(10)
                    enemy_killed = True
                    break
                while quick_user_input_1 == "2":
                    print("You throw the body aside, refusing to indulge in your dark desires!")
                    enemy_killed = True
                    break
            if quick_user_input == "" and time_passed > time_limit:
                character.lose_health(health_lost)




#FOUND BY 1 GUARD FUNCTION
def attacked_by_one_guard(time_limit_for_sequence, room):
    time.sleep(2.5)
    quick_time_event(main_character, time_limit_for_sequence, 30, room)

def restart_program():
    subprocess.run(["python", "main.py"])

def ask_if_play_again():
    print("Would you like to play again?")
    options(end_prompt_list, end)
    end_user_input = input(">>> ")
    if end_user_input == "1":
        restart_program()
    elif end_user_input == "2":
        print("Thanks for playing!")
        time.sleep(1)
        raise SystemExit

def ominous_spirit_stare_ending():
    if prisoners_free == False:
        print("'Oh, for fucks sake!' the spirit rages. 'How can one little human be so annoying?!'")
        print("'Fine, go through. See if I care. Just stop staring at me. Please.'")
        print("The spirit moves aside and you rush past, afraid he'll rescind his offer.")
        print("Soon you come to the end of the tunnel. The air smells fresh. Like pines and clear sky.")
        print("You take one final look back. Misery. A bad dream, and nothing more.")
        print("You're free.")
        #CREDITS GO HERE
        notebook.reset_notebook()
        ask_if_play_again()
    else:
        print("'Oh, for fucks sake!' the spirit rages. 'How can one little human be so annoying?!'")
        print("'Fine, go through. See if I care. Just stop staring at me. Please.'")
        print("'Wait one second' you say, risking the wrath of the Ominous Spirit. You sprint back ")
        print("to the Jail and grab the prisoners, hauling them back with you to the tunnel. You ")
        print("keep your head down as you pass the Ominous Spirit. Soon you come to the end of the ")
        print("tunnel. The air smells fresh. Like pines and clear sky. You take one final look back.")
        print("Misery. A bad dream, and nothing more. You're free. And what's more, the prisoners are, too.")
        print("Your heart unclenches.")
        #CREDITS GO HERE
        notebook.reset_notebook()
        ask_if_play_again()
        

def ominous_spirit_riddle_ending():
    print("If the spirit had a brow, it would be furrowed. He stands in silence for a moment, as though trying ")
    print("to figure out how you did it. After some time, he snaps out of it and his eyes focus on you. ")
    print("'You're not like the others... I don't know how, or why, but you're not. And for that, I give you this: ")
    main_character.inv.add_item("Spirit's Blessing")
    print("You feel a rush wash over you, and your bloodlust fades. You look to the spirit, but he simply moves aside. ")
    print("You keep your head down as you pass the Ominous Spirit. Soon you come to the end of the ")
    print("tunnel. The air smells fresh. Like pines and clear sky. You take one final look back.")
    print("Misery. A bad dream, and nothing more. You're free.")
    print("Your heart unclenches, and you move onwards, propelled by the Ominous Spirit's blessing.")
    #CREDITS GO HERE
    notebook.reset_notebook()
    ask_if_play_again()


def main_door_full_blood_glut_ending():
    print("You look back at the wretched place that contained you for so long, wondering if setting it ablaze would be too much.")
    print("It's not worth it, you think. There's prey to hunt, and the darkness calls you forward.")
    print("You throw an impossbily-strong kick, ripping the large wooden doors off their hinges and stepping outside.")
    print("Your skin boils in the sunlight as the slaves run past you, fear-struck by your smoking form. You have become everything you hate.")
    print("The last thing you remember the unbearably hot sun beating down, melting your flesh...")
    #ASCII ART GOES HERE "THE END"
    notebook.reset_notebook()
    ask_if_play_again()


#CHANCE OF AN EVENT WORKING
# chance = Chance()
# chance.chance_of_success(3)

# #ADD ITEM
# main_character.inv.add_item("Sheild")
# #DISPLAY STATS
# main_character.check_stats()

# #ADD BLOOD GLUT
# main_character.add_blood_glut(100)

#ADD TIME DELAY TO PRINT
# time.sleep(1)

#ROOMS
cell = Room("Cell", [])
jail = Room("Jail", [""])
treasury = Room("Treasury", ["Gold key"])
tunnel = Room("Tunnel", [""])
armoury = Room("Armoury", ["Sword"])
dracula_chambers = Room("Dracula's Chambers", ["Master Key"])
prompt = "What do you want to do?"
end = Room("End", [])


#CELL LOGIC
cell_prompt_list_1_1 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks.",
                "Exit the cell door.",]
cell_prompt_list_1_2 = ["Snap a femur and shave it down to a sizeable 'key'", 
                        "Whittle a splinter of bone down to a needle for... engraving.",
                        "Go back"]
#"Examine the bloody basin."
cell_prompt_list_2_1 = ["Take a sip",
                      "Look underneath",
                      "Go back"]

#CELL ROOM LOGIC

cell_room_prompt_list_1_1 = ["Enter Treasury Room.",
                             "Free the prisoners.",
                             "Enter Armoury. (* 100% chance of conflict *)",
                             "Try the door to freedom",
                             "Check engraving on the door.",
                             "Go back into the Cell"]
#TREASURY LOGIC
treasury_prompt_list_1_1 = ["Drain the servant",
                             "Examine the gold coins",
                             "Knock the servant unconscious",
                             "Examine door at the back of the room",
                             "Go back to the Jail."]
#Examine the gold coins
treasury_prompt_list_1_2 = ["Bite the coin.",
                             "Forge a key out of the gold coins.",
                             "Go back.",]
#Examining the door at the back of the room
treasury_prompt_list_1_3 = ["Dig away some of the coins. (* 20% chance of conflict *)",
                             "Check the letter on the table besides the door.",
                             "Go back."]

treasury_prompt_list_1_3_1 = ["Step over the gold and enter the door.",
                             "Check the letter on the table besides the door.",
                             "Go back."]
#Opening the door in the treasury
tunnel_prompt_list_1 = ["Venture down the tunnel.",
                             "Go back."]
tunnel_prompt_list_2 = ["Bow before the figure.",
                        "Ask to pass.",
                        "Stand and stare in awkward silence.",
                        "Go back."]

tunnel_prompt_list_2_1 = ["Bow before the figure.",
                        "Try the riddle.",
                        "Stand and stare in awkward silence.",
                        "Go back."]

armoury_prompt_list_1 = ["Charge the men head on."]

armoury_prompt_list_2 = ["Back into the doorway to draw them in one at a time.",
                         "Charge them head on."]

armoury_prompt_list_3 = ["Go forward to Dracula's Chambers.",
                         "Loot the soldier's bodies."
                         "Go back."]

dracula_prompt_list_1 = ["'You deserve to die for what you've done to these people.'",
                         "'You've lived for long enough, don't you think?'",
                         "'Actually, I've left a pile of bodies behind me the whole way here. I have zero moral agency.'"
                         "Go back."]


end_prompt_list = ["Yes",
                   "No"]



print("You awaken in a castle cell. Blood drips steadily from the bricks above, splashing into a rusty basin. The moans of distant prisoners fill the halls. (TODO. TAPTAPTAP.sleep(1)) In the corner is a pile of bones. Past prisoners.")
print("The bite marks on your body are from him: Dracula. You're his personal blood bag.")
print("Something's different, though. Your bite marks are healing, and the strength in your limbs wills you to fight back. What's happening to you?")
time.sleep(1)
while True:
    display_stats()
    options(cell_prompt_list_1_1, cell)
    user_input = input(">>> ")
    # TODO: MAKETHIS A FUNCTION INCLUDING ALL USER INPUTS
    if main_character.inv.has_item("Bone Pen"):
        if user_input == "write" or user_input == "Write":
            append_arm()
        else:
            pass
    if main_character.health <= 0:
        #GAME OVER DUE TO MISSING HEALTH FUNCTION GOES HERE (This only needs to be attached to instances of health loss)
        pass
    while user_input == "1":
        if main_character.bloodglut < 20:
            print("You walk over to the pile of bones.")
            print("Poor chap, you think. Lazily, your eyes drift over to the cell door, then back to the bones. Hmmm... If only you were stronger...")
            break
        elif main_character.bloodglut >= 20:
            options(cell_prompt_list_1_2, cell)
            user_input_1_2 = input(">>> ")
            while user_input_1_2 == "1":
                if main_character.inv.has_item("Bone Key"):
                    print("You've already done this.")
                    break
                else:
                    print("It takes some doing, but you manage to snap it in half.")
                    main_character.inv.add_item("Bone Key")
                    break
            while user_input_1_2 == "2":
                if main_character.inv.has_item("Bone Pen"):
                    print("You've already done this.")
                    break
                else:
                    print("Time drags on, but eventually you make a pen for... writing.")
                    print("HINT: Type 'Write' into the terminal to carve text into your arm.")
                    main_character.inv.add_item("Bone Pen")
                    break
            if user_input_1_2 == "3":
                print("You go back.")
                break

    while user_input == "2":
        print("You check the basin. The blood is as much mud as it is blood. You revolt.")
        options(cell_prompt_list_2_1, cell)
        user_input_2_1 = input(">>> ")
        while user_input_2_1 == "1":
            if main_character.bloodglut >= 20:
                print("You've already done this.")
                break
            else:
                main_character.add_blood_glut(20)
                break
        while user_input_2_1 == "2":
            print("You kneel down and look under the sink to see someone has engraved some text.")
            print("'Something always yearns. Don't ever accept this hell.'")
            break
        if user_input_2_1  == "3":
            break
        
    while user_input == "3":
        print("'Help me', calls one prisoner. 'Please', calls another. They're Dracula's play things. Nothing to him but chaffe. Your will cements. You must escape.")
        break

    while user_input == "4":
        print("You reach your arms up, looking closely at the bite marks made by Dracula. You think of the countless times you've been fed on and you seethe...")
        time.sleep(1)
        break
    
    while user_input == "5":
        exit_cell_room = False
        if cell_door_open == True:
            print("You step through the opened cell door.")
        elif main_character.inv.has_item("Bone Key"):
            cell_door_open = True
            print("You jam the bone key into the cell door keyhole, breaking it but snapping the lock open at the same time. The door slides wide open and you step through into a hallway.")
            main_character.inv.remove_item("Bone Key")
            print("The prisoners moan and wail at you to let them out. To the left of you is a door labelled 'Treasury'. You can hear coins clinking behind it, but no speaking.")
            print("To your right is a door named 'Armoury'. Behind it, Dracula's guards laugh and joust.")
            print("Before you is a wide door that appears to lead outside.")
            cell_door_opened_once = True
        else:
            if cell_door_opened_once:
                print("You step through the cell door without needing a key.")
            else:
                print("It's not particularly well built. If only we had some way to open it...")
            break
        while cell_door_open and not exit_cell_room:
            display_stats()
            options(cell_room_prompt_list_1_1, jail)
            cell_room_user_input = input(">>> ")
            while cell_room_user_input == "1":
                if tresury_entered == False:
                    tresury_entered = True
                    print("Silently, you enter a well lit room with piles upon piles of golden coins strewn about the place.")
                    print("A blind servant sits at a rickety table, counting coins and placing them into bags.")
                    display_stats()
                    options(treasury_prompt_list_1_1, treasury)
                    treasury_room_user_input = input(">>> ")
                else:
                    print("You're standing in the Treasury.")
                    display_stats()
                    options(treasury_prompt_list_1_1, treasury)
                    treasury_room_user_input = input(">>> ")
                while treasury_room_user_input == "1":
                    if servant_killed == False:
                        print("You sieze the servant, ripping into his neck and drinking deeply. With nobody to stop you,")
                        print("you're able to drink your fill.")
                        main_character.add_blood_glut(30)
                        servant_killed = True
                        break
                    elif servant_unconscious == True:
                        print("A change of heart, eh?")
                        print("You pick the man up off the floor and tear into his neck. With nobody to stop you,")
                        print("you're able to drink your fill.")
                        main_character.add_blood_glut(30)
                        servant_killed = True
                    else:
                        print("He can't get any dead-er than he is.")
                        break
                while treasury_room_user_input == "2":
                    print("You examine the gold coins.")
                    display_stats()
                    options(treasury_prompt_list_1_2, treasury)
                    treasury_room_user_input_1 = input(">>> ")
                    while treasury_room_user_input_1 == "1":
                        print("Your teeth sink straight through the metal. Yep, that's real gold alright.")
                        break
                    while treasury_room_user_input_1 == "2":
                        if main_character.inv.has_item("Gold Key"):
                            print("You've already done that.")
                            break
                        else:
                            print("You grab a couple gold coins and get to work, compressing them like clay and fashioning yourself a key.")
                            main_character.inv.add_item("Gold Key")
                            break
                    if treasury_room_user_input_1 == "3":
                        break
                while treasury_room_user_input == "3":
                    if servant_unconscious == False and servant_killed == False:
                        print("With a hard backhand, you clop the servant over the head. He falls to the ground,")
                        print("moaning for a moment before going still. His wheezing breaths fill the chamber. How annoying.")
                        servant_unconscious = True
                        break
                    elif servant_killed == True:
                        print("You've just killed the man. Doesn't get much more 'unconscious' than that, does it?")
                        break
                    else:
                        print("He's already unconscious. Give the man a break.")
                        break
                while treasury_room_user_input == "4":
                    if servant_unconscious == False and servant_killed == False:
                        print("You can't do that yet, you'll be heard!")
                        break
                    else:
                        print("You approach the door, which is mostly-obscured by piles of coins.")
                        display_stats()
                        if tunnel_door_opened:
                            options(treasury_prompt_list_1_3_1, treasury)
                        else: 
                            options(treasury_prompt_list_1_3, treasury)
                        treasury_room_user_input_2 = input(">>> ")
                        while treasury_room_user_input_2 == "1":
                            if dig_counter >= 3:
                                tunnel_door_opened = True
                                print("You stand before a dark tunnel with a yellow glowing light at the end of it.")
                                display_stats()
                                options(tunnel_prompt_list_1, tunnel)
                                treasury_room_user_input_3 = input(">>> ")
                                while treasury_room_user_input_3 == "1":
                                    if tunnel_travelled_down == False:
                                        print("You venture down the tunnel, closing the distance between you and the yellow light.")
                                        print("As you near, you realise it's not a light, but two lights. You go to turn back, but ")
                                        print("a voice calls to you, telling you to come closer. You take the chance, and soon find ")
                                        print("yourself standing before a shadowy figure with two monstrous eyes. The figure hovers ")
                                        print("before a tunnel.")
                                        tunnel_travelled_down = True
                                    display_stats()
                                    if asked_riddle == False:
                                        options(tunnel_prompt_list_2, tunnel)
                                    else:
                                        options(tunnel_prompt_list_2_1, tunnel)
                                    tunnel_user_input_2 = input(">>> ")
                                    while tunnel_user_input_2 == "1":
                                        if bowed_before_ominous_spirit == False:
                                            print("'What is this? Get up. Bow again and rip you to shreds,' he says.")
                                            print("How pleasant.")
                                            bowed_before_ominous_spirit = True
                                            break
                                        else:
                                            print("'What, you thought I was joking?'")
                                            print("The Ominous Spirit lashes out.")
                                            main_character.lose_health(40)
                                            break
                                    while tunnel_user_input_2 == "2":
                                        if main_character.bloodglut <= 50:
                                            print("Look at you - all gorged on blood. And now you want my help? I don't think so.")
                                            break
                                        if asked_riddle == False:
                                            print("'Hmm, interesting proposition,' says the Ominous Spirit. 'I'll tell you what - ")
                                            print("if you can answer my riddle, I'll let you go. Here it is: ")
                                            print("'I'm the timeless enigma, lurking somwhere between future and past.")
                                            print("To me, a sharpened pencil is closer than an unsharpened one.")
                                            print("I was before, and I will be again.")
                                            print("What am I?'")
                                            asked_riddle = True
                                        else:
                                            print("'Back to make another guess? Come on then, let's hear it.'")
                                            print("'Here's the riddle again, in case you've forgotten. You probably have:'")
                                            print("'I'm the timeless enigma, lurking somwhere between future and past.")
                                            print("To me, a sharpened pencil is closer than an unsharpened one.")
                                            print("I was before, and I will be again.")
                                            print("What am I?'")
                                        tunnel_user_input_3 = input(">>> ")
                                        if tunnel_user_input_3 == "Death" or tunnel_user_input_3 == "death":
                                            ominous_spirit_riddle_ending()
                                        else:
                                            print("Ha. Nice try, but you'll have to try harder.")
                                            break
                                    while tunnel_user_input_2 == "3":
                                        if ominous_spirit_stare_counter > 19:
                                            ominous_spirit_stare_ending()
                                        elif ominous_spirit_stare_counter < 5:
                                            print("The Ominous Spirit stares straight back at you, piercing your very soul. Something ")
                                            print("inside you goes cold. You shiver.")
                                            ominous_spirit_stare_counter += 1
                                            break
                                        elif ominous_spirit_stare_counter >= 5 and ominous_spirit_stare_counter < 10:
                                            print("'What?' the Ominous Spirit asks. 'Why are you staring?'")
                                            print("You smile.")
                                            ominous_spirit_stare_counter += 1
                                            break
                                        elif ominous_spirit_stare_counter >= 10 and ominous_spirit_stare_counter < 15:
                                            print("The Spirit appears to be losing his composition. You keep smiling.")
                                            ominous_spirit_stare_counter += 1  
                                            break
                                        elif ominous_spirit_stare_counter >= 15 and ominous_spirit_stare_counter <= 19:
                                            print("He begins to sweat. Your smile widens.")
                                            ominous_spirit_stare_counter += 1 
                                            break
                                    if tunnel_user_input_2 == "4":
                                        break
                                if treasury_room_user_input_3 == "2":
                                    break
                            chance_of_success(3)
                            if tunnel_door_opened == False:
                                if chance_of_success(3) == "Your attempt fails!":
                                    dig_counter += 1
                                    print("A guard stumbles into the room, sword half unsheathed, drawn in by the tinkling of coins.")
                                    attacked_by_one_guard(2.5, treasury)
                                    treasury_guard_dead = True
                                else:
                                    print("You dig successfully without being heard!")
                                    dig_counter += 1
                                break
                            else:
                                break
                        if treasury_room_user_input_2 == "2":
                            print("It reads: 'No bloodbag is to enter here until I've dealt with it's occupant.'")
                            print("Signed: Dracula")
                        if treasury_room_user_input_2 == "3":
                            break
                if treasury_room_user_input == "5":
                    break
            while cell_room_user_input == "2":
                if prisoners_free:
                    print("You've already done that.")
                    break
                elif main_character.inv.has_item("Bone Key"):
                    print("You're resourceful, aren't you?")
                    print("You go back and forth, forging bone-shaped keys and smashing them into the locks one by one.")
                    print("The prisoners have been freed! They huddle around the main door, too scared to do anything else.")
                    prisoners_free = True
                    break
                elif main_character.bloodglut < 50:
                    print("You try and bend the bars, but they won't give. If only you were stronger...")
                    break
                elif prisoners_free == True:
                    print("They're already free.")
                else:
                    print("Strength swells within you. With your newfound might, you snap the bars off their hinges. ")
                    print("The prisoners have been freed!")
                    prisoners_free = True
                    break
            while cell_room_user_input == "3":
                if main_character.inv.has_item("Gold Key"):
                    if armoury_entered == False:
                        print("You open the Armoury door to find 3 guards, all with plate armour and weapons. They drop their drinks and draw their swords.")
                        armoury_entered = True
                        display_stats()
                        options(armoury_prompt_list_1, armoury)
                        armoury_user_input_1 = input(">>> ")
                        while armoury_prompt_list_1 == "1":
                            print("You lunge at the closest one, who raises his sword in defense. You dodge.")
                            time.sleep(2)
                            attacked_by_one_guard(2.0, armoury)
                            print("Done with the first one, the other two charge you.")
                            display_stats()
                            options(armoury_prompt_list_2, armoury)
                            armoury_user_input_2 = input(">>> ")
                            if armoury_user_input_2 == "1":
                                print("You edge backwards, forcing them to face you one at a time.")
                                time.sleep(2)
                                attacked_by_one_guard(2.0, armoury)
                                display_stats()
                                print("Done with the first, the other looks hesitant to approach you. You take the fight to him.")
                                time.sleep(2)
                                attacked_by_one_guard(2.0, armoury)
                                display_stats()
                                break
                            elif armoury_user_input_2 == "2":
                                print("Blindly, you rush both of them and get attacked twice in a short period.")
                                time.sleep(1.5)
                                attacked_by_one_guard(1.5, armoury)
                                display_stats()
                                time.sleep(1)
                                attacked_by_one_guard(1, armoury)
                                display_stats()
                                break

                    else:
                        print("You stand in the armoury, surveying the carnage you've caused.")
                        display_stats()
                        options(armoury_prompt_list_3, armoury)
                        armoury_user_input_3 = input(">>> ")
                        while armoury_user_input_3 == "1":
                            print("With a looming silence, you press forwards, inching the doors to Dracula's chamber open.")
                            print("It's daytime, so you expect a sleeping figure hanging from the ceiling. You've never")
                            print("been more incorrect.")
                            print("Resting on a velvet throne is Dracula in a full set of engraved metal armour. In those")
                            print("carvings you see a million deaths. A million lifetimes spent drinking blood. Dracula smiles,")
                            print("her spectacularly white teeth sparkling between her frame of golden hair. She stands from her")
                            print("throne, a devious smile spread upon her lips.")
                            print("'I can only presume you're here to kill me,' she says, her smirk growing wider.")
                            display_stats()
                            options(dracula_prompt_list_1, dracula_chambers)
                            dracula_chambers_user_input_3 = input(">>> ")
                            if dracula_chambers_user_input_3 == "1":
                                pass
                            if dracula_chambers_user_input_3 == "2":
                                pass
                            if dracula_chambers_user_input_3 == "3":
                                pass
                            if dracula_chambers_user_input_3 == "4":
                                pass


                        if armoury_user_input_3 == "2":
                            print("With thoughts of facing Dracula armed, you reach for their weapons and armour,")
                            print("only to find they're made of silver and hot to the touch.")
                            main_character.lose_health(5)
                            print("'Curse this affliction,' you murmur.")
                        if armoury_user_input_1 == "3":
                            break



                else:
                    print("It appears you need some sort of metal key to do that. Maybe you can make one?")
                    break
            while cell_room_user_input == "4":
                if main_character.bloodglut < 65:
                    print("You need either the Master Key or the strength to brute force it.")
                    break
                elif main_character.bloodglut > 65:
                        main_door_full_blood_glut_ending()
            while cell_room_user_input == "5":
                print("You step closer, reading the quote plainly with your imporved vision.")
                print("'I'll tear spleens, defeat everything and this hell to get what I want.'")
                break
            if cell_room_user_input == "6":
                exit_cell_room = True
        
        if exit_cell_room:
            break
            