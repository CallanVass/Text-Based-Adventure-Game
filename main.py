from classes import *
from hueprint import cprint
from hueprint.types import EColour, EEffect
import time



# #NOTEBOOK FUNCTION
# notebook = Notebook()

# notebook.read_notebook()
# notebook.write_notebook()

#Character Creation
main_character = Character("Argus")
#QUICKTIME EVENT WORKING
fight = Fight()
fight.quick_time_event(main_character, 2, 30)
main_character.check_stats()


# #ADD ITEM
# main_character.inv.add_item("Sheild")
# #DISPLAY STATS
# main_character.check_stats()

# #ADD BLOOD GLUT
# main_character.add_blood_glut(100)


# main_character.check_stats()
