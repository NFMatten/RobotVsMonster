from weapons import Weapon
import time
# Purpose: Create "robot" object, takes in "weapon" object. 
class Robot:
    def __init__(self, name):
        self.name = name #string
        self.health = 100 #int
        self.active_weapon = Weapon("Blaster Cannon", 10) #object

    def attack(self, dinosaur):
        pause_duration = 1
        time.sleep(pause_duration) # Slows program to see each attack more clearly
        dinosaur.health -= self.active_weapon.attack_power
        print(f'Robot {self.name} attacked {dinosaur.name} with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage!')
        print(f'{dinosaur.name} has {dinosaur.health} health remaining!\n')