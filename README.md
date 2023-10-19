# Text-Based-Adventure-Game

# ==================================**Spoilers Ahead**===========================================


## R3 Bibliography/References:



## R4 Github Link:

[Repository link](https://github.com/CallanVass/Text-Based-Adventure-Game)



## R5 Style Guide:

Styling convention follows what is essentially PEP8, but simplified.

[Here is the guide](https://www.tutorialspoint.com/coding-standards-style-guide-for-python-programs)



## R6 List Of Features:

### Feature 1 -- Changeable Notebook

- On ever decision tree will be a changeable notebook as the first option. Upon selecting the notebook, it will open and allow you to either write in it or simply view it. The user can use this feature however they like, although it would be best for them to use it to record the quotes they come accross.

### Feature 2 -- Blood Glut Meter

- A meter that is set to 0 upon initialization of the program, the blood glut meter will update upon consuming blood, allowing the user access to better percentage chances of completing certain actions, but at the same time hindering others. One example is that the Ominous Spirit will not allow you to attempt the riddle if you're above 60 blood glut. Another is that if you exit the door with 100 blood glut (meaning you've turned into a vampire), you will burn in the sun, which is still a valid ending, just not a happy one.

### Feature 3 -- Multiple Rooms/Ways To Escape

- The game will have 3 endings. The first is solving the riddle and escaping past the Ominous Spirit, the second is gaining the master key from the armoury and escaping with the slaves, the third is defeating Dracula and escaping (this kills the player). There is another option, which is to cram the slaves back into their cells and remain as master of the castle.



## R7 Checklist Of Features:

### Feature 1 -- Changeable Notebook

- .txt file is called via the Options class using the open() fuction

- .txt file is opened with the "r" function, allowing the user to see past writings

- .txt file is appended by user using the open() function with an "a" for append

- Appended text is saved to the .txt file due to using the with open() as f: function

- TODO: Add notebook to list of actions displayed to user (in 1st place) (Will only be possible once options class is sorted)



### Feature 2 -- Blood Glut Meter

- Set to 0 by attaching it to the character class with a hardcoded value.

- Nest blood glut with option-handling while loops that run the main() program. Only if certain actions are completed is it to be increased.

- Tie blood glut meter to escape ending where player burns. Using conditional statemets such as if blood_glut => 100 for certain endings.

- Display blood glut meter at the top of the terminal options with every choice. This will simply be a matter of setting a "getter" method within the character class. Such as Character.get_glut_meter().

- Ensure there are options that player cannot complete if blood_glut_meter isn't high enough (e.g freeing the slaves). if blood_glut_meter < 50, can't complete action.


### Feature 3 -- Multiple Rooms/Ways To Escape

- Create Room class to contain individual rooms to certain blocks of code. class = Room

- Write base script for each room in the main section, then move it to suit individual needs. 

- Contain options to lists of printed statements so that options can be referenced by their index, such as Room[0][0].

- Use break statements to finish while loops to create alternate endings.

- Attach the inventory class to the rooms for items that can be picked up. I'll do this by using comprehension. E.g self.inv = Inventory[]


TODO: TALK ABOUT THE OTHER FEATURES ONCE THEY'RE CONFIRMED TO HAVE BEEN BUILT
## R8 Installation instructions:
