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

- A meter that is set to 0 upon initialization of the program, the blood satiation meter will update upon consuming blood, allowing the user access to better percentage chances of completing certain actions, but at the same time hindering others. One example is that the Ominous Spirit will not allow you to attempt the riddle if you're above 60 blood glut. Another is that if you exit the door with 100 blood glut (meaning you've turned into a vampire), you will burn in the sun, which is still a valid ending, just not a happy one.

### Feature 3 -- Multiple Rooms/Ways To Escape

- The game will have 3 endings. The first is solving the riddle and escaping past the Ominous Spirit, the second is gaining the master key from the armoury and escaping with the slaves, the third is defeating the Dracula and escaping (this kills the player). There is another option, which is to cram the slaves back into their cells and remain as master of the castle.



## R7 Checklist Of Features:

### Feature 1 -- Changeable Notebook

- .txt file is called via the Options class using the open() fuction

- .txt file is opened with the "r" function, allowing the user to see past writings

- .txt file is appended by user using the open() function with an "a" for append

- Appended text is saved to the .txt file due to using the with open() as f: function

- TODO: Add notebook to list of actions displayed to user (in 1st place) (Will only be possible once options class is sorted)



### Feature 2 -- Blood Glut Meter


### Feature 3 -- Multiple Rooms/Ways To Escape


## R8 Installation instructions:
