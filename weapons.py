# Purpose: "Weapon" object creation for the robot object

class Weapon:
    def __init__(self, name, attack_power):
        """
        Purpose: Creates weapon object
        Parameters:
            name: string
            attack_power: int
        """
        self.name = name #string
        self.attack_power = attack_power # int