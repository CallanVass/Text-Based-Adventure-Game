class Character:
    def __init__(self, name, health, bloodlust):
        self.name = name
        self.health = health
        self.bloodlust = f"{bloodlust}/100"
        self.inv = Inventory()
    
    def check_inventory(self):
        print(self.inv)

class Inventory:
    def __init__(self):
        self.items = []

    def add_items(self, name):
        items = Inventory
        self.items.append(name)
    


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

class Options:
    pass

class Chance:

    def chance_of_success(percentage):
        pass

class Main:
    pass

class Room:
    def room_inventory(self):
        self.inv = Inventory([])


