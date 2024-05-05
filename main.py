
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

