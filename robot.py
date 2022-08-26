from weapons import Weapon
import time
from random import choice
# Purpose: Create "robot" object, takes in "weapon" object. 
class Robot:
    def __init__(self, name):
        """
        Purpose: Create robot object
        Parameter: 
            name: string
        """
        self.name = name
        self.health = 100 
        self.active_weapon = self.choose_active_weapon()
        

    def choose_active_weapon(self):
        blaster_rifle = Weapon("Blaster Rifle", 10)
        rocket_launcher = Weapon("Rocket Launcher", 15)
        thermal_detonator = Weapon("Thermal Detonator", 20)
        weapons_list = [blaster_rifle, rocket_launcher, thermal_detonator]
        active_weapon = choice(weapons_list)
        return active_weapon

    def attack(self, dinosaur):
        """
        Purpose: Conducts attack on to opponent
        Parameter:
            dinosaur: object
        """
        pause_duration = 1
        time.sleep(pause_duration) # Slows program to see each attack more clearly

        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health < 0:
            dinosaur.health = 0
        print(self.attack_string(dinosaur))
        

    def attack_string(self, dinosaur):
        """
        Purpose: Display string during attack
        Parameter: 
            dinosaur: object
        """
        attack_string = f'''
        Robot {self.name} attacked {dinosaur.name} with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage!
        {dinosaur.name} has {dinosaur.health} health remaining!
        '''
        return attack_string