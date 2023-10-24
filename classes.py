import time
import random
from main import ask_if_play_again
from main import 

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.bloodglut = 0
        self.inv = Inventory()
    
    def check_stats(self):
        return f"Health: {self.health}/100    Blood Glut: {self.bloodglut}/100\nInventory: {self.inv.get_items()}"

    def check_dracula_stats(self):
        return f"Dracula's Health: {self.health}/100"

    def lose_health(self, health_loss):
        self.health -= health_loss
        print(f"You lose {health_loss} health!")

    def dracula_health_loss(self, health_loss):
        self.health -= health_loss
        print(f"Dracula loses {health_loss} health!")
    
    def check_health(self, health):
        if self.health <= 0:
            notebook.reset_notebook()
            ask_if_play_again()

    def add_blood_glut(self, amount):
        self.bloodglut = self.bloodglut + amount
        increase = f"Blood Glut has been increased by {amount}!"
        if self.bloodglut > 100:
            self.bloodglut = 100
        if self.bloodglut <= 20:
            print(f"{increase} Dark desires writhe within you!")
        elif self.bloodglut > 20 and self.bloodglut <= 50:
             print(f"{increase} You grow stronger and an almost irresistable desire for blood awakens!")
        elif self.bloodglut > 50 and self.bloodglut <= 65:
             print(f"{increase} You're turning into an unkillable creature of nightmares!")
        elif self.bloodglut > 65 and self.bloodglut <= 80:
             print(f"{increase} You swelter with violent power. Soon you'll be lost to your human form forever!")
        elif self.bloodglut > 80 and self.bloodglut <= 99:
             print(f"{increase} Your humanity sinks deeper with every kill, drowned in the blood of your enemies! One more kill and you'll be lost to the dark forces of vampirism!")
        else:
            print(f"{increase} Darkness shrouds around you like torrent of black fire, hailing you as its new king!")

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name):
        self.items.append(name)
        print(f"You have picked up: {name}!")

    def remove_item(self, name):
        self.items.remove(name)
        print(f"You have lost: {name}!")

    def get_items(self):
        return self.items
    
    def has_item(self, name):
        return name in self.items
    
class Notebook:
    def read_notebook(self):
        with open("notebook.txt", "r") as file:
            file_writings = file.read()
            print("You look at your arm.")
            print(file_writings)

    def write_notebook(self):
        with open("notebook.txt", "a") as file:
            user_input = input("What would you like to carve? ")
            file.write(f"{user_input}\n")
    
    def reset_notebook(self):
        with open("notebook.txt", "w") as file:
            pass

class Chance:
    def chance_of_success(self, percentage):
        random_nums = [random.randint(1, 10) for _ in range(percentage)]
        if percentage == 1:
            if 1 in random_nums:
                print("Your attempt fails!")
            else:
                print("Your attempt succeeds!")
        if percentage == 2:
            if any(value in random_nums for value in (1, 2)):
                print("Your attempt fails!")
            else:
                print("Your attempt succeeds!")
        if percentage == 3:
            if any(value in random_nums for value in (1, 2, 3)):
                print("Your attempt fails!")
            else:
                print("Your attempt succeeds!")
        if percentage >= 4:
            print("Callan, you dolt, that's a stupidly high percentage. Change it right now.")

class Room:
    def __init__(self, name, inv):
        self.inv = Inventory()
        self.name = name   
    
    def get_name(self):
        print(f"You are currently in the {self.name}.")

