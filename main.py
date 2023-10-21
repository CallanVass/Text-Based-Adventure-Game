from classes import *
import time
import random

#NOTEBOOK FUNCTION
def append_arm():
    notebook = Notebook()
    notebook.read_notebook()
    notebook.write_notebook()
    return

#OPTIONS FUNCTION
def options(option_list):
    cell.get_name()
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

def main_door_full_blood_glut_ending():
    print("You look back at the wretched place that contained you for so long, wondering if setting it ablaze would be too much.")
    print("It's not worth it, you think. There's prey to hunt, and the darkness calls you forward.")
    print("You throw an impossbily-strong kick, ripping the large wooden doors off their hinges and stepping outside.")
    print("Your skin boils in the sunlight as the slaves run past you, fear-struck by your smoking form. You have become everything you hate.")
    print("The last thing you remember the unbearably hot sun beating down, melting your flesh...")
    #ASCII ART GOES HERE "THE END"
#QUICKTIME EVENT WORKING
# fight = Fight()
# fight.quick_time_event(main_character, 2, 30)
# main_character.check_stats()

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
#Character Creation
notebook = Notebook()
main_character = Character("Argus")
#ROOMS
cell = Room("Cell", ["Bone Pen", "Bone Key"])
jail = Room("Jail", [""])
treasury = Room("Treasury", ["Gold key"])
tunnel = Room("Tunnel", [""])
armoury = Room("Armoury", ["Sword"])
master_chambers = Room("Master Chambers", ["Master Key"])
prompt = "What do you want to do?"


#CELL LOGIC
cell_prompt_list_1_1 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks.",
                "Exit the cell door.",]
                #Original option: "Try the cell door."
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
                             "Enter Armoury.",
                             "Try the door to freedom",
                             "Go back into the Cell"]





print("You awaken in a castle cell. Blood drips steadily from the bricks above, splashing into a rusty basin. The moans of distant prisoners fill the halls. (TODO. TAPTAPTAP.sleep(1)) In the corner is a pile of bones. Past prisoners.")
print("The bite marks on your body are from him: Dracula. You're his personal blood bag.")
print("Something's different, though. Your bite marks are healing, and the strength in your limbs wills you to fight back. What's happening to you?")
time.sleep(1)
while True:
    # cell_door_open = False
    display_stats()
    options(cell_prompt_list_1_1)
    user_input = input(">>> ")
    # TODO: MAKETHIS A FUNCTION INCLUDING ALL USER INPUTS
    if main_character.inv.has_item("Bone Pen"):
        if user_input == "write" or user_input == "Write":
            append_arm()
        else:
            pass

    while user_input == "1":
        if main_character.bloodglut < 20:
            print("You walk over to the pile of bones.")
            print("Poor chap, you think. Lazily, your eyes drift over to the cell door, then back to the bones. Hmmm... If only you were stronger...")
            break
        elif main_character.bloodglut >= 20:
            options(cell_prompt_list_1_2)
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
        options(cell_prompt_list_2_1)
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
        cell_door_open = False
        if main_character.inv.has_item("Bone Key"):
            if cell_door_open == True:
                continue
            cell_door_open = True
            print("You jam the bone key into the cell door keyhole, breaking it but snapping the lock open at the same time. The door slides wide open and you step through into a hallway.")
            main_character.inv.remove_item("Bone Key")
            print("The prisoners moan and wail at you to let them out. To the left of you is a door labelled 'Treasury'. You can hear coins clinking behind it, but no speaking.")
            print("To your right is a door named 'Armoury'. Behind it, Dracula's guards laugh and joust.")
            print("Before you is a wide door that appears to lead outside.")
            while True:
                display_stats()
                options(cell_room_prompt_list_1_1)
                cell_room_user_input = input(">>> ")
                while cell_room_user_input == "1":
                    pass
                while cell_room_user_input == "2":
                    if main_character.bloodglut < 50:
                        print("You try and bend the bars, but they won't give. If only you were stronger...")
                        break
                    elif main_character.inv.has_item("Bone Key"):
                        print("You're resourceful, aren't you?")
                        print("You go back and forth, forging bone-shaped keys and smashing them into the locks one by one.")
                        print("The prisoners have been freed!")
                        prisoners_free = True
                        #Watch this logic for reoccuring instances (ability to do it multiple times)
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
                        print("You open the Armoury door to find 3 guards, all with plate armour and weapons. They drop their drinks and draw their swords.")
                        #ARMOURY LOGIC GOES HERE
                    else:
                        print("It appears you need a key to do that. Maybe you can make one?")
                        break
                while cell_room_user_input == "4":
                    if main_character.bloodglut < 65:
                        print("You need either the Master Key or the strength to brute force it.")
                        break
                    elif main_character.bloodglut > 65:
                            main_door_full_blood_glut_ending()
                if cell_room_user_input == "5":
                    break
                
                
        else:
            print("It's not particularly well built. If only we had some way to open it...")
            break
        
    

