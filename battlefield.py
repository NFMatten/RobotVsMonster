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
        message = f"\nWelcome to the Battlefield! \nToday's challengers:\n{self.robot.name} vs. {self.dinosaur.name}"
        return message

    def battle_phase(self):
        """
        Purpose: Conducts battle until one opponent's health reaches zero
        """
        winner_chosen = False
        while winner_chosen == False:
            if self.robot.health != 0:
                self.robot.attack(self.dinosaur)
                if self.dinosaur.health == 0:
                    winner_chosen = True

            if self.dinosaur.health != 0:
                self.dinosaur.attack(self.robot)
                if self.robot.health == 0:
                    winner_chosen = True
        winner = self.determine_winner()
        return winner

    def determine_winner(self):
        """
        Purpose: Determine winner by checking health of each opponent
        """
        if self.robot.health <= 0:
            winner = self.dinosaur.name
        if self.dinosaur.health <= 0:
            winner = self.robot.name
        return winner

    def display_winner(self):
        """
        Purpose: Displays who won battle
        """
        winner = self.battle_phase()
        return f'{winner} wins!\n'
