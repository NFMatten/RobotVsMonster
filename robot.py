from weapons import Weapon
import time
# Purpose: Create "robot" object, takes in "weapon" object. 
class Robot:
    def __init__(self, name):
        """
        Purpose: Create robot object
        Parameter: 
            name: string
        """
        self.name = name #string
        self.health = 100 #int
        self.active_weapon = Weapon("Blaster Cannon", 10) #object

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
        attack_string = f'''
        Robot {self.name} attacked {dinosaur.name} with a {self.active_weapon.name} for {self.active_weapon.attack_power} damage!
        {dinosaur.name} has {dinosaur.health} health remaining!
        '''
        return attack_string