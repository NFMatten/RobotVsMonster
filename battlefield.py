from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        """
        Purpose: Creates robot and dinosaur objects for this battlefield object
        """
        self.robot = Robot("C-3PO")
        self.dinosaur = Dinosaur("Rex", 15)
        
    def run_game(self):
        """
        Purpose: Run the game once called
        """
        print(self.display_welcome())
        print(self.display_winner())

    def display_welcome(self):
        """
        Purpose: Displays welcome message. (Message below is poorly written via code)
        """
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
        """
        Purpose: Conducts battle until one opponent's health reaches zero
        """
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

            # Determine winner (Can be a seperate method)
            if self.robot.health <= 0:
                winner = self.dinosaur.name
            elif self.dinosaur.health <= 0:
                self.dinosaur.health = 0
                winner = self.robot.name
        return winner

    def display_winner(self):
        """
        Purpose: Displays who won battle
        """
        winner = self.battle_phase()
        return f'{winner} wins!\n'
