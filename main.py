import threading
import time
import os

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# Class for the Virtual Pet
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self._fullness = 50
        self._happiness = 50
        self._energy = 50
    # Ensures that the pet's status is always changing while running
        self.is_running = True
        self.game_over = False
    # Text for feeding pet
    def feed(self):
        print(f"You have put food out for {self.name}")
        time.sleep(1)
        print("CHOMP")
        time.sleep(1)
        print("CHOMP")
        time.sleep(1)
        print("CHOMP")
        time.sleep(2)
        print(f"The food is all gone and {self.name} is feeling stuffed!")
        time.sleep(1)

        self._fullness += 20
        self._happiness += 20
        self._energy += 10

    def play(self):
        # Text for playing with virtual pet
        print(f"{self.name} wants to play fetch")
        time.sleep(1)
        print("You have thrown the ball")
        time.sleep(1)
        print(f"{self.name} is running for the ball")
        time.sleep(2)
        print(f"{self.name} is still running for the ball")
        time.sleep(1)
        print(f"{self.name} is bringing the ball back")
        time.sleep(2)
        print(f"Wow that was fun! {self.name} is feeling happier now!")
        time.sleep(1)
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
        print(f"{self.name} is awake and refreshed")

        self._fullness = 50
        self._happiness = 50
        self._energy = 50

    # Starting the timer that alters pets status over time
    def start_timer(self):
        self.timer_thread = threading.Thread(target=self.alter_attributes)
        self.timer_thread.start()
        
    # Stopping the timer that alters pets status over time
    def stop_timer(self):
        self.is_running = False

    # Setting the limits for the pets attributes
    def confirm_attribute(self, attribute, max_value, message):
        if attribute <= 0:
            print(message["min"])
            self.game_over = True
        elif attribute == max_value:
            print(message["warning"])
        elif attribute > max_value:
            print(message["max"])
            self.game_over = True

    # Quits the loop before displaying messages if game is over
    def confirm_attributes(self):
        if self.game_over:
            if os.path.exists("pet_status.txt"):
                os.remove("pet_status.txt")
                return
            return

        fullness_message = {
            "min": (f"\n{Fore.RED}{Style.BRIGHT}{self.name} has died of starvation"),
            "warning": (f"\n{Fore.RED}{Style.BRIGHT}{self.name} is full, stop before they explode!"),
            "max": (f"\n{Fore.RED}{Style.BRIGHT}{self.name} ate so much they burst!")
        }

        happiness_message = {
            "min": (f"\n{Fore.RED}{Style.BRIGHT}{self.name} has died of loneliness"),
            "warning": (f"\n{Fore.RED}{Style.BRIGHT}{self.name}'s heart is full of sunshine and rainbows, be careful they can't take much more!"),
            "max": (f"\n{Fore.RED}{Style.BRIGHT}Too much sunshine, now {self.name} is dead!")
        }

        energy_message = {
            "min": (f"\n{Fore.RED}{Style.BRIGHT}{self.name} has run out of energy"),
            "warning": (f"\n{Fore.RED}{Style.BRIGHT}{self.name} if full, of energy! someone better play with them!"),
            "max": (f"\n{Fore.RED}{Style.BRIGHT}The buildup of energy inside {self.name} has converted to heat and roasted them!")
        }
        self.confirm_attribute(self._fullness, 100, fullness_message)
        self.confirm_attribute(self._happiness, 100, happiness_message)
        self.confirm_attribute(self._energy, 100, energy_message)


    def alter_attributes(self):
        while self.is_running:
            self.confirm_attributes()
            if self.game_over:
                break
            self._fullness -= 2
            self._happiness -= 2
            self._energy += 1
            time.sleep(5)

    def status(self):
        return (f"\n{Style.BRIGHT}{Fore.BLUE}Name:{Fore.RESET} {self.name}, {Style.BRIGHT}{Fore.BLUE}Hunger:{Fore.RESET} {self._fullness}, {Style.BRIGHT}{Fore.BLUE}Happiness:{Fore.RESET} {self._happiness}, {Style.BRIGHT}{Fore.BLUE}Energy:{Fore.RESET} {self._energy}\n")


# Menu Screen
def create_menu(pet):
        
    print(pet.status())

    print(Fore.BLUE + Style.BRIGHT +"Press "+ Fore.MAGENTA + "ENTER/RETURN" + Fore.BLUE + Style.BRIGHT + Back.RESET + " to refresh")
    print(Fore.BLUE + Style.BRIGHT +"Press "+ Fore.MAGENTA + "1" + Fore.BLUE + Style.BRIGHT + Back.RESET + " to feed your pet")
    print(Fore.BLUE + Style.BRIGHT +"Press "+ Fore.MAGENTA + "2" + Fore.BLUE + Style.BRIGHT + Back.RESET + " to let your pet rest")
    print(Fore.BLUE + Style.BRIGHT +"Press "+ Fore.MAGENTA + "3" + Fore.BLUE + Style.BRIGHT + Back.RESET + " to to play with your pet")
    print(Fore.BLUE + Style.BRIGHT +"Press "+ Fore.MAGENTA + "4" + Fore.BLUE + Style.BRIGHT + Back.RESET + " to EXIT")

    user_choice = input(Fore.MAGENTA + Style.BRIGHT + "\nPick your action: " + Fore.RESET)
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
    # Opens the file storing pet data if available, if not, prompts for pet name
    pet_info = load_status()
    if pet_info:
        print(f"\n{Fore.BLUE}{Style.BRIGHT}Welcome to your Virtual Pet Simulator, {pet_info[0]} has been waiting for you!{Back.RESET}\n")
        pet = VirtualPet(pet_info[0])
        pet._fullness = pet_info[1]
        pet._happiness = pet_info[2]
        pet._energy = pet_info[3]
    else:
        print(Fore.BLUE + Style.BRIGHT + "Welcome to your Virtual Pet Simulator!")
        pet_name = input(Fore.BLUE + Style.BRIGHT + "What's your pet's name?: " + Fore.RESET)
        pet = VirtualPet(pet_name)

    pet.start_timer()

    choice = ""
    while choice != "4" and pet.game_over == False:
        choice = create_menu(pet)
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.rest()
        elif choice == "3":
            pet.play()
        elif choice == "4":
            print("Exiting Application...")
            pet.stop_timer()
            save_status(pet)
            break
        elif choice == "":
            continue
        else:
            print(Back.RED+ Style.BRIGHT + "\nInvalid Input, please select from numbers 1-4" + Back.RESET)

    print(Fore.MAGENTA + Style.BRIGHT + "Thank you for playing! See you soon!")
    pet.confirm_attributes()
    exit()

if __name__ == "__main__":
    main()
