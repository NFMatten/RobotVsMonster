import time
# Purpose: Create "monster" object
class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name #string
        self.health = 100 #int
        self.attack_power = attack_power #int

    def attack(self, robot):
        pause_duration = 1
        time.sleep(pause_duration) # Slows program to see each attack more clearly
        
        robot.health -= self.attack_power
        if robot.health < 0:
            robot.health = 0
        print(f'Dinosaur {self.name} attacked {robot.name} for {self.attack_power} damage!')
        print(f'{robot.name} has {robot.health} health remaining!\n')
