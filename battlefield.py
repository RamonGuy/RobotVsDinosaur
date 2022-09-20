

from robot import Robot 
from dinosaur import Dinosaur
class Battlefield:
    def __init__(self) -> None:
        self.player1 = Robot()
        self.player2 = Dinosaur()



    def display_welcome(self):
     print("Hello to the Robot-Vs-Dinosaur Game")

    def battle_phase(self):
            while self.player1.health > 0 and self.player2.health > 0:
                self.player1.attack_dinosaur(Dinosaur())
                self.player2.attack_robot(Robot())
                print('')


    def display_winner(self):
        if self.player1.health == 0:
            print(f'{self.player2} is the winner')
        elif self.player2 == 0:
            print(f'{self.player1} is the winner')
        else:
            print("Sorry nobody won this time!!!")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()