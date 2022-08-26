from robot import Robot
from dinosaur import Dinosaur

# Purpose: Creates "battlefield" object, should take in "robot" and "monster" objects
class Battlefield:
    def __init__(self):
        self.robot = Robot("C-3PO")
        self.dinosaur = Dinosaur("Rex", 15)
        
    def run_game(self):
        print(self.display_welcome())
        print(self.display_winner())

    def display_welcome(self):
        message = f'''
        *******************************
        * Welcome to the battlefield! *
        *                             *
        *     Today's challengers:    *
        *  \t{self.robot.name} vs. {self.dinosaur.name}\t      *
        *******************************
        '''
        return message

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

            # Determine winner
            if self.robot.health <= 0:
                winner = self.dinosaur.name
            elif self.dinosaur.health <= 0:
                self.dinosaur.health = 0
                winner = self.robot.name
        return winner

    # Purpose: Prints who won
    def display_winner(self):
        winner = self.battle_phase()
        return f'{winner} wins!\n'
