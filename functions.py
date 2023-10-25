#IMPORTS
from classes import *
import time
import random
import subprocess
from colour_text import ColourText

ct = ColourText()
ct.initTerminal()

#GLOBAL FLAG VARIABLES
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
guard_killed_counter = 0
bowed_before_ominous_spirit = False
tunnel_prompt_list_1_asked = False
main_character_is_vampire = False
treasury_guard_dead = False
armoury_guards_dead = False
armoury_entered = False
dracula_killed = False
dracula_chambers_entered = False
attack_counter = 0

#ROOM OBJECTS
cell = Room("Cell", [])
jail = Room("Jail", [""])
treasury = Room("Treasury", ["Gold key"])
tunnel = Room("Tunnel", [""])
armoury = Room("Armoury", ["Sword"])
dracula_chambers = Room("Final Chambers", ["Master Key"])
prompt = "What do you want to do?"
end = Room("End", [])

#DEFINING MAIN CHARACTER AND NOTEBOOK
notebook = Notebook()
main_character = Character("Argus")
dracula = Character("Dracula")

#APPEND NOTEBOOK
def append_arm():
    notebook = Notebook()
    notebook.read_notebook()
    notebook.write_notebook()
    return
#APPEND FUCTION ATTACHED TO INSTANCES OF USER INPUT
def can_write(input):
    if main_character.inv.has_item("Bone Pen"):
        if input == "write" or input == "Write":
            append_arm()
        else:
            pass

#OPTIONS FUNCTION
def options(option_list, room):
    time.sleep(0.3)
    room.get_name()
    for index, option in enumerate(option_list):
        print(ct.convert(f"<>cyan Option {index + 1}:<> {option}"))
        time.sleep(0.2)
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

#CHECKING CHARACTER HEALTH FUNCTION
def check_character_health():
    if main_character.health <= 0:
        you_died()
        time.sleep(5)
        ask_if_play_again()

#FOUND BY 1 GUARD FUNCTION (TREASURY AND ARMOURY)
def attacked_by_one_guard(time_limit_for_sequence, room):
    time.sleep(1.5)
    quick_time_event(main_character, time_limit_for_sequence, 30, room)

#RESTART PROGRAM FUNCTION
def restart_program():
    subprocess.run(["python", "main.py"])

#ASK TO PLAY AGAIN FUNCTION
def ask_if_play_again():
    print("Would you like to play again?")
    options(end_prompt_list, end)
    end_user_input = input(">>> ")
    if end_user_input == "1":
        restart_program()
    elif end_user_input == "2":
        print("Thanks for playing!")
        raise SystemExit

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

#FIGHT EVENT FUNCTION
def quick_time_event(character, time_limit, health_lost, room):
    enemy_killed = False
    quick_time_prompt_list = ["Drain them dry!",
                                "Knock them unconscious!"]
    while enemy_killed == False:
        start = time.time()
        quick_user_input = input(f"Quickly, press Enter!: ")
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
                global guard_killed_counter
                guard_killed_counter += 1
                break
            while quick_user_input_1 == "2":
                print("You throw the body aside, refusing to indulge in your dark desires!")
                enemy_killed = True
                break
        if quick_user_input == "" and time_passed > time_limit:
            character.lose_health(health_lost)
            check_character_health()

#DRACULA FIGHT EVENT FUNCTION
def fight_with_dracula(character, time_limit, health_lost):
    start = time.time()
    quick_user_input = input(f"Quickly press Enter to fight back: ")
    end = time.time()
    time_passed = end - start
    global attack_counter
    attack_counter =+ 1
    while attack_counter == 1:
        if quick_user_input == "" and time_passed < time_limit:
            print("You dodge her feral claws and throw back an attack of your own, catching her unaware")
            dracula.dracula_health_loss(20)
            break
        if quick_user_input == "" and time_passed > time_limit:
            print("It slashes you across the chest, drawing thick blood to the surface.")
            character.lose_health(health_lost)
            check_character_health()
            break
    while attack_counter == 2:
        if quick_user_input == "" and time_passed < time_limit:
            print("You catch the attack, slashing her across the throat with claws of your own.")
            dracula.dracula_health_loss(20)
            break
        if quick_user_input == "" and time_passed > time_limit:
            print("The attack slams you into a wall. You bounce back, coughing up blood.")
            character.lose_health(health_lost)
            check_character_health()
            break
    while attack_counter == 3:
        if quick_user_input == "" and time_passed < time_limit:
            print("She dives left, but you catch her attack just before it lands, rerouting the momentum.")
            dracula.dracula_health_loss(20)
            break
        if quick_user_input == "" and time_passed > time_limit:
            print("Her attack circumnavigates your defence, piercing your ribs and puncturing a lung.")
            character.lose_health(health_lost)
            check_character_health()
            break
    while attack_counter == 4:
        if quick_user_input == "" and time_passed < time_limit:
            print("You're too quick, and catch her hand just before it smashes into your jaw.")
            dracula.dracula_health_loss(20)
            break
        if quick_user_input == "" and time_passed > time_limit:
            print("Her hand cracks you in the jaw. You turn back, dazed.")
            character.lose_health(health_lost)
            check_character_health()
            break
    while attack_counter == 5:
        if quick_user_input == "" and time_passed < time_limit:
            print("You're too quick, and catch her hand just before it smashes into your jaw.")
            dracula.dracula_health_loss(20)
            break
        if quick_user_input == "" and time_passed > time_limit:
            print("Her hand cracks you in the jaw. You turn back, dazed.")
            character.lose_health(health_lost)
            check_character_health()
            break

#INTRO FUNCTION 
def intro():
    print("You awaken in a castle cell. Blood drips steadily from the bricks above, splashing into a rusty basin.")
    time.sleep(2)
    print("Tap...")
    time.sleep(1.5)
    print("Tap...")
    time.sleep(1.5)
    print("Tap...")
    time.sleep(1.5)
    print("The moans of distant prisoners fill the halls. In the corner is a pile of bones. Past prisoners.")
    time.sleep(0.3)
    print("The bite marks on your body are from Dracula. You're a blood slave. Something's different, though.")
    time.sleep(0.3)
    print("Your bite marks are healing, and the strength in your limbs wills you to fight back.")
    time.sleep(0.3)
    print("What's happening to you?")

#BELOW ARE ENDING FUCTIONS. TITLES ARE INDICATIVE
def self_bludgeon_ending():
    print("The thought of actually trying makes you extremely fed up.")
    time.sleep(0.3)
    print("Welp, you think, I guess this is better than round-the-clock-torture.")
    time.sleep(0.3)
    print("Then again... you think, but before you can change your mind, you")
    time.sleep(0.3)
    print("slip on a small pool of blood smack your head on the sink. Nice one,")
    time.sleep(0.3)
    print("doofus.")
    time.sleep(12)
    #CREDITS GO HERE
    notebook.reset_notebook()
    ask_if_play_again()

def ominous_spirit_stare_ending():
    if prisoners_free == False:
        print("'Oh, for fucks sake!' the spirit rages. 'How can one little human be so annoying?!'")
        time.sleep(0.3)
        print("'Fine, go through. See if I care. Just stop staring at me. Please.'")
        time.sleep(0.3)
        print("The spirit moves aside and you rush past, afraid he'll rescind his offer.")
        time.sleep(0.3)
        print("Soon you come to the end of the tunnel. The air smells fresh. Like pines and clear sky.")
        time.sleep(0.3)
        print("You take one final look back. Misery. A bad dream, and nothing more.")
        time.sleep(0.3)
        print("You're free.")
        time.sleep(15)
        #CREDITS GO HERE
        notebook.reset_notebook()
        ask_if_play_again()
    else:
        print("'Oh, for fucks sake!' the spirit rages. 'How can one little human be so annoying?!'")
        time.sleep(0.3)
        print("'Fine, go through. See if I care. Just stop staring at me. Please.'")
        time.sleep(0.3)
        print("'Wait one second' you say, risking the wrath of the Ominous Spirit. You sprint back ")
        time.sleep(0.3)
        print("to the Jail and grab the prisoners, hauling them back with you to the tunnel. You ")
        time.sleep(0.3)
        print("keep your head down as you pass the Ominous Spirit. Soon you come to the end of the ")
        time.sleep(0.3)
        print("tunnel. The air smells fresh. Like pines and clear sky. You take one final look back.")
        time.sleep(0.3)
        print("Misery. A bad dream, and nothing more. You're free. And what's more, the prisoners are, too.")
        time.sleep(0.3)
        print("Your heart unclenches.")
        time.sleep(15)
        #CREDITS GO HERE
        notebook.reset_notebook()
        ask_if_play_again()
        
def ominous_spirit_riddle_ending():
    if prisoners_free == False:
        print("If the spirit had a brow, it would be furrowed. He stands in silence for a moment, as ")
        time.sleep(0.3)
        print("though trying to figure out how you did it. After some time, he snaps out of it and his ")
        time.sleep(0.3)
        print("eyes focus on you.")
        time.sleep(0.3)
        print("'You're not like the others... I don't know how, or why, but you're not. And for that, ")
        time.sleep(0.3)
        print("I give you this: ")
        time.sleep(0.3)
        main_character.inv.add_item("Spirit's Blessing")
        time.sleep(0.3)
        print("You feel a rush wash over you, and your bloodlust fades. You look to the spirit, but he  ")
        time.sleep(0.3)
        print("simply moves aside. You keep your head down as you pass the Ominous Spirit. Soon you")
        time.sleep(0.3)
        print("come to the end of the tunnel. The air smells fresh. Like pines and clear sky. You take")
        time.sleep(0.3)
        print("one final look back. Misery. A bad dream, and nothing more. You're free.")
        time.sleep(0.3)
        print("Your heart unclenches, and you move onwards, propelled by the Ominous Spirit's blessing.")
        time.sleep(18)
        #CREDITS GO HERE
        notebook.reset_notebook()
        ask_if_play_again()
    else:
        print("If the spirit had a brow, it would be furrowed. He stands in silence for a moment, as ")
        time.sleep(0.3)
        print("though trying to figure out how you did it. After some time, he snaps out of it and his ")
        time.sleep(0.3)
        print("eyes focus on you.")
        time.sleep(0.3)
        print("'You're not like the others... I don't know how, or why, but you're not. And for that, ")
        time.sleep(0.3)
        print("I give you this: ")
        time.sleep(0.3)
        main_character.inv.add_item("Spirit's Blessing")
        time.sleep(0.3)
        print("You feel a rush wash over you, and your bloodlust fades. You look to the spirit, but he  ")
        time.sleep(0.3)
        print("simply moves aside." )
        time.sleep(0.3)
        print("'Wait one second' you say, risking angering of the Ominous Spirit. You sprint back ")
        time.sleep(0.3)
        print("to the Jail and grab the prisoners, hauling them back with you to the tunnel.")
        time.sleep(0.3)
        print("You keep your head down as you pass the Ominous Spirit. Soon you")
        time.sleep(0.3)
        print("come to the end of the tunnel. The air smells fresh. Like pines and clear sky. You take")
        time.sleep(0.3)
        print("one final look back. Misery. A bad dream, and nothing more. You're free. They're free.")
        time.sleep(0.3)
        print("Your heart unclenches, and you move onwards, propelled by the Ominous Spirit's blessing.")
        time.sleep(20)
        #CREDITS GO HERE
        notebook.reset_notebook()
        ask_if_play_again()

def main_door_full_blood_glut_ending():
    if prisoners_free == False:
        print("First, you free the prisoners with your immense strength.")
        time.sleep(0.3)
    print("You look back at the wretched place that contained you for so long, wondering if setting ")
    time.sleep(0.3)
    print("it ablaze would be too much. It's not worth it, you think. There's prey to hunt, and the")
    time.sleep(0.3)
    print("darkness calls you forward. You throw an impossbily-strong kick, ripping the large wooden")
    time.sleep(0.3)
    print("doors off their hinges and stepping outside. Your skin boils in the sunlight as the prisoners")
    time.sleep(0.3)
    print("run past you, fear-struck by your smoking form. You have become everything you hate.")
    time.sleep(0.3)
    print("The last thing you remember is the unbearably hot sun beating down, melting your flesh...")
    time.sleep(18)
    #ASCII ART GOES HERE "THE END"
    notebook.reset_notebook()
    ask_if_play_again()

def main_door_ending_with_key():
    print("You look back at the wretched place that contained you for so long, wondering if setting it")
    time.sleep(0.3)
    print("ablaze would be too much. It's not worth it, you think. Maybe one day, someone will live ")
    time.sleep(0.3)
    print("here. Someone nice. Someone kind. You insert the Master Key into the lock and swing the large ")
    time.sleep(0.3)
    print("wooden doors forward, stepping outside. Your skin tingles in the sunlight, a ghost of the ")
    time.sleep(0.3)
    print("pain it might have caused you if you'd transitioned.The last thing you remember are the prisoners ")
    time.sleep(0.3)
    print("rushing past you, free at last.")
    time.sleep(0.3)
    print("You smile. It's finally over.")
    time.sleep(18)
    #ASCII ART GOES HERE "THE END"
    notebook.reset_notebook()
    ask_if_play_again()

def main_door_ending_without_key():
    print("You look back at the wretched place that contained you for so long, wondering if setting it")
    time.sleep(0.3)
    print("ablaze would be too much.It's not worth it, you think. Maybe one day, someone will live here.")
    time.sleep(0.3)
    print("Someone nice. Someone kind. You throw an impossbily-strong kick, ripping the large wooden doors ")
    time.sleep(0.3)
    print("off their hinges and stepping outside. Your skin tingles in the sunlight, a ghost of the pain ")
    time.sleep(0.3)
    print("it might have caused you if you'd transitioned.The last thing you remember are the prisoners ")
    time.sleep(0.3)
    print("rushing past you, free at last.")
    time.sleep(0.3)
    print("You smile. It's finally over.")
    time.sleep(18)
    #ASCII ART GOES HERE "THE END"
    notebook.reset_notebook()
    ask_if_play_again()

def dracula_spared_ending():
    print("'You're right,' you say, giving into your own darkness.")
    time.sleep(0.3)
    print("Slowly, you remove your hand from her neck and stand up.")
    time.sleep(0.3)
    print("Dracula slowly stands. 'Just wait until I show you all we can do,' she cooes.")
    time.sleep(0.3)
    print("'Come now, my child. The night is still young, and there is blood to be spilt.'")
    time.sleep(0.3)
    print("As night falls, you both head to a nearby town. Terror ensues. The screams of the")
    time.sleep(0.3)
    print("innocent echo off every wall in the town. ")
    time.sleep(0.3)
    print("You've become a prince of darkness.")
    time.sleep(18)
    #ASCII ART GOES HERE "THE END"
    notebook.reset_notebook()
    ask_if_play_again()

#ASCII ART FUNCTIONS
def draculas_castle():
    print(ct.convert("<>magenta ▓█████▄  ██▀███   ▄▄▄       ▄████▄   █    ██  ██▓    ▄▄▄        ██████     ▄████▄   ▄▄▄        ██████ ▄▄▄█████▓ ██▓    ▓█████  ▐██▌ <>"))
    print(ct.convert("<>magenta ▒██▀ ██▌▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██  ▓██▒▓██▒   ▒████▄    ▒██    ▒    ▒██▀ ▀█  ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓██▒    ▓█   ▀  ▐██▌ <>"))
    print(ct.convert("<>magenta ░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓██  ▒██░▒██░   ▒██  ▀█▄  ░ ▓██▄      ▒▓█    ▄ ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒██░    ▒███    ▐██▌ <>"))
    print(ct.convert("<>magenta ░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓▓█  ░██░▒██░   ░██▄▄▄▄██   ▒   ██▒   ▒▓▓▄ ▄██▒░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒██░    ▒▓█  ▄  ▓██▒ <>"))
    print(ct.convert("<>magenta ░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒▒█████▓ ░██████▒▓█   ▓██▒▒██████▒▒   ▒ ▓███▀ ░ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░██████▒░▒████▒ ▒▄▄  <>"))
    print(ct.convert("<>magenta  ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░ ░▀▀▒ <>"))
    print(ct.convert("<>magenta  ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░     ░  ▒     ▒   ▒▒ ░░ ░▒  ░ ░    ░    ░ ░ ▒  ░ ░ ░  ░ ░  ░ <>"))
    print(ct.convert("<>magenta  ░ ░  ░   ░░   ░   ░   ▒   ░         ░░░ ░ ░   ░ ░    ░   ▒   ░  ░  ░     ░          ░   ▒   ░  ░  ░    ░        ░ ░      ░       ░ <>"))
    print(ct.convert("<>magenta    ░       ░           ░  ░░ ░         ░         ░  ░     ░  ░      ░     ░ ░            ░  ░      ░               ░  ░   ░  ░ ░    <>"))
    print(ct.convert("<>magenta  ░                         ░                                              ░                                                         <>"))

def you_died():
    print(ct.convert("<>red  ▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄<>"))
    print(ct.convert("<>red  ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌<>"))
    print(ct.convert("<>red   ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌<>"))
    print(ct.convert("<>red   ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌<>"))
    print(ct.convert("<>red   ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓ <>"))
    print(ct.convert("<>red    ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒ <>"))
    print(ct.convert("<>red  ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒ <>"))
    print(ct.convert("<>red  ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░ <>"))
    print(ct.convert("<>red  ░ ░         ░ ░     ░           ░     ░     ░  ░   ░    <>"))
    print(ct.convert("<>red  ░ ░                           ░                  ░      <>"))

#OPTION LISTS FOR EACH ROOM
#CELL LISTS
cell_prompt_list_1_1 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks.",
                "Exit the cell door.",]

cell_prompt_list_1_2 = ["Snap a femur and shave it down to a sizeable 'key'", 
                        "Whittle a splinter of bone down to a needle for... engraving.",
                        "Go back"]

cell_prompt_list_2_1 = ["Take a sip",
                      "Look underneath",
                      "Bludgeon yourself on the basin.",
                      "Go back"]

#CELL ROOM LISTS
cell_room_prompt_list_1_1 = ["Enter Treasury Room.",
                             "Free the prisoners.",
                             "Enter Armoury. (* 100% chance of conflict *)",
                             "Try the door to freedom",
                             "Check carving on the door.",
                             "Go back into the Cell"]

cell_room_prompt_list_1_2 = ["Enter Treasury Room.",
                             "Free the prisoners.",
                             "Enter Armoury.",
                             "Try the door to freedom",
                             "Check engraving on the door.",
                             "Go back into the Cell"]

#TREASURY LISTS
treasury_prompt_list_1_1 = ["Drain the servant",
                             "Examine the gold coins",
                             "Knock the servant unconscious",
                             "Examine door at the back of the room",
                             "Go back to the Jail."]

treasury_prompt_list_1_2 = ["Bite the coin.",
                             "Forge a key out of the gold coins.",
                             "Go back.",]

treasury_prompt_list_1_3 = ["Dig away some of the coins. (* 20% chance of conflict *)",
                             "Check the letter on the table besides the door.",
                             "Go back."]

treasury_prompt_list_1_3_1 = ["Step over the gold and enter the door.",
                             "Check the letter on the table besides the door.",
                             "Go back."]

#TUNNEL LISTS
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

#ARMOURY LISTS
armoury_prompt_list_1 = ["Charge the men head on."]

armoury_prompt_list_2 = ["Back into the doorway to draw them in one at a time.",
                         "Charge them again."]

armoury_prompt_list_3 = ["Go forward to Dracula's Chambers.",
                         "Loot the soldier's bodies.",
                         "Go back."]

#DRACULA'S ROOM LISTS
dracula_prompt_list_1 = ["'You deserve to die for what you've done to these people.'",
                         "'You've lived for long enough, don't you think?'",
                         "'Actually, I've left a pile of bodies behind me the whole way here. I have zero moral agency.'",
                         "Enough chit chat. Let's fight.",
                         "Go back."]

dracula_prompt_list_2 = ["'You deserve to die for what you've done to these people.'",
                         "'You've lived for long enough, don't you think?'",
                         "'I'm not entirely exempt, either. But you need to be stopped'",
                         "'Enough chit chat. Let's fight.'",
                         "Go back."]

dracula_prompt_list_2_1 = ["'There is no redemption for you!' (Kill Dracula)",
                         "I suppose... I suppose that could work. (Spare Dracula)"]

dracula_prompt_list_3 = ["Exit the room."]

#END PROMPT LIST
end_prompt_list = ["Yes",
                   "No"]

