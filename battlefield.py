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
        while c3po.health > 0 and rex.health > 0:
            time.sleep(pause_duration)
            print(f"{c3po.name} attacked {rex.name} with a {c3po.active_weapon.name}\nRex Health: {rex.health}")
            c3po.attack(rex)
            rex.attack(c3po)
            print(f"C-3PO Health: {c3po.health}\t ")
            print()
            if c3po.health <= 0:
                c3po.health = 0
                print("C3PO lost")
            elif rex.health <= 0:
                rex.health = 0
                print("Rex lost")

    def display_winner(self):
        c3po = Robot("C-3PO")
        rex = Dinosaur("Rex", 15)
        if c3po.health <= 0:
            print("Rex wins!")
        elif rex.health <= 0:
            print("C-3PO wins!")
