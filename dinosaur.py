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
        self.name = name
        self.health = 100
        self.attack_power = attack_power

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
        print(self.attack_string(robot))

    def attack_string(self, robot):
        """
        Purpose: Display string during attack
        Parameter: 
            robot: object
        """
        attack_string = f'''
        Dinosaur {self.name} attacked {robot.name} for {self.attack_power} damage!
        {robot.name} has {robot.health} health remaining!
        '''
        return attack_string