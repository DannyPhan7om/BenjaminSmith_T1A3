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