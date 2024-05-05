import threading
import sys
import time


# Class for the Virtual Pet
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self._fullness = 50
        self._happiness = 50
        self._energy = 50

    def feed(self):
        self._fullness += 20
        self._happiness += 20
        self._energy += 10

    def play(self):
        self._fullness -= 20
        self._happiness += 20
        self._energy -= 10

    def rest(self):
        # Added some snoring to personalise the game
        print(f"{self.name} is counting sheep to get to sleep")
        time.sleep(1) 
        print("1 sheep")
        time.sleep(1)
        print("2 sheep")
        time.sleep(1)
        print("3 she--")
        time.sleep(1)
        print(f"{self.name} is fast asleep")
        time.sleep(2)
        print("honk")
        time.sleep(1)
        print("shuuu")
        time.sleep(1)
        print("honk")
        time.sleep(1)
        print("shuuuuu")
        time.sleep(2)
        print(f"{self.name} is awake and refreshed, stats are back to baseline")

        self._fullness = 50
        self._happiness = 50
        self._energy = 50

    

    def status(self):
        return f"Name: {self.name}, Hunger: {self._fullness}, Happiness: {self._happiness}, Energy: {self._energy}"


# Menu Screen
def create_menu(pet):

    print(pet.status())

    print("1. Press 1 to feed your pet")
    print("2. Press 2 to let your pet rest")
    print("3. Press 3 to play with your pet")
    print("4. Press 4 to EXIT")

    user_choice = input("Pick your action:  ")
    print(user_choice)
    return user_choice

# Ability to Save Pet Status at end of gaming session
def save_status(pet):
    with open("pet_status.txt", "w") as f:
        f.write(f"{pet.name}\n")
        f.write(f"{pet._fullness}\n")
        f.write(f"{pet._happiness}\n")
        f.write(f"{pet._energy}\n")


# Ability to Load Pet Status at start of gaming session
def load_status():
    try:
        with open("pet_status.txt", "r") as f:
            name = f.readline().strip()
            fullness = int(f.readline().strip())
            happiness = int(f.readline().strip())
            energy = int(f.readline().strip())
            return name, fullness, happiness, energy
    except FileNotFoundError:
        return None

# Actions from the menu
def main():
    # Opens the file storing peta data if available, if not, prompts for pet name
    pet_info = load_status()
    if pet_info:
        print(f"Welcome to your Virtual Pet Simulator, {pet_info[0]} has been waiting for you!")
        pet = VirtualPet(pet_info[0])
        pet._fullness = pet_info[1]
        pet._happiness = pet_info[2]
        pet._energy = pet_info[3]
    else:
        print("Welcome to your Virtual Pet Simulator!")
        pet_name = input("What's your pet's name?: ")
        pet = VirtualPet(pet_name)


    choice = ""
    while choice != "4":
        choice = create_menu(pet)
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.rest()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            print("Exiting Application...")
            save_status(pet)
        else:
            print("Invalid Input, please select from numbers 1-4")

    print("Thank you for playing! See you soon!")
    exit()

if __name__ == "__main__":
    main()