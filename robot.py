from weapons import Weapon

# Purpose: Create "robot" object, takes in "weapon" object. 
class Robot:
    def __init__(self, name):
        self.name = name #string
        self.health = 100 #int
        self.active_weapon = Weapon("Blaster Cannon", 10) #object

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power