from robot import Robot
from dinosaur import Dinosaur
import time

# Purpose: Creates "battlefield" object, should take in "robot" and "monster" objects
class Battlefield:
    def __init__(self):
        c3po = Robot("C-3PO")
        rex = Dinosaur("Rex", 15)
        pass

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle_phase():
        c3po = Robot("C-3PO")
        rex = Dinosaur("Rex", 15)
        pause_duration = 1
        # Continues fight until one opponent health reaches 0 
        while c3po.health > 0 and rex.health > 0:
            time.sleep(pause_duration) # Slows program to see each attack more clearly

            # c3po attacks
            c3po.attack(rex)
            print(f"{c3po.name} attacked {rex.name} with a {c3po.active_weapon.name} for {c3po.active_weapon.attack_power}\nRex Health: {rex.health}")
            # rex attacks
            rex.attack(c3po)
            print(f"{rex.name} attacked {c3po.name} for {rex.attack_power}. C-3PO Health: {c3po.health}")
            # if opponent loses, print winner (To be updated with "display_winner" method)
            if c3po.health <= 0:
                c3po.health = 0
                print("C3PO lost")
            elif rex.health <= 0:
                rex.health = 0
                print("Rex lost")

    # Purpose: Prints who won
    def display_winner(self):
        c3po = Robot("C-3PO")
        rex = Dinosaur("Rex", 15)
        if c3po.health <= 0:
            print("Rex wins!")
        elif rex.health <= 0:
            print("C-3PO wins!")
