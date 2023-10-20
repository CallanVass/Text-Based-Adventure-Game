from classes import *
import time
import random

#NOTEBOOK FUNCTION
def append_arm():
    notebook = Notebook()
    notebook.read_notebook()
    notebook.write_notebook()
    return

notebook = Notebook()

#Character Creation
main_character = Character("Argus")
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

#ROOMS
cell = Room("Cell", ["Bone shard", "Bone Key"])
jail = Room("Jail", [""])
treasury = Room("Treasury", ["Gold key"])
tunnel = Room("Tunnel", [""])
armoury = Room("Armoury", ["Sword"])
master_chambers = Room("Master Chambers", ["Master Key"])
prompt = "What do you want to do?"

def options(option_list):
    for index, option in enumerate(option_list):
        print(f"Option {index + 1}: {option}")
    return
        

# while True:
#CELL LOGIC
print("You awaken in a castle cell. Blood drips steadily from the bricks above, splashing into a rusty basin. The moans of distant prisoners fill the halls. (TODO. TAPTAPTAP.sleep(1)) In the corner is a pile of bones. Past prisoners.")


print(f"You are currently in the {cell.get_name()}")

cell_prompt_list_1_1 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks."]
#"Examine the bloody basin."
cell_prompt_list_2 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks."]
#Listen out to the calls of the prisoners.
cell_prompt_list_3 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks."]
#Examine bite marks.
cell_prompt_list_4 = ["Examine the pile of bones.", 
                "Examine the bloody basin.", 
                "Listen out to the calls of the prisoners.", 
                "Examine bite marks."]


print(main_character.check_stats())
print(prompt)
options(cell_prompt_list_1_1)

input()
# if input() == "1":
options(cell_prompt_list_2)

