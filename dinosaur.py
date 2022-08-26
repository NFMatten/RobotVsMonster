
# Purpose: Create "monster" object
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name #string
        self.health = 100 #int
        self.attack_power = attack_power #int

    def attack(self, robot):
        robot.health -= self.attack_power
