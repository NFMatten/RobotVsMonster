import time
# Purpose: Create "monster" object
class Dinosaur:
    def __init__(self, name, attack_power):
        """
        Purpose: Create dinosaur object
        Parameters: 
            name: string
            attack_power: int 
        """
        self.name = name #string
        self.health = 100 #int
        self.attack_power = attack_power #int

    def attack(self, robot):
        """
        Purpose: Conducts attack on to opponent
        Parameter:
            robot: object
        """
        pause_duration = 1
        time.sleep(pause_duration) # Slows program to see each attack more clearly

        robot.health -= self.attack_power
        if robot.health < 0:
            robot.health = 0
        print(f'Dinosaur {self.name} attacked {robot.name} for {self.attack_power} damage!')
        print(f'{robot.name} has {robot.health} health remaining!\n')
