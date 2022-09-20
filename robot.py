
from weapon import Weapon



class Robot:
    def __init__(self) -> None:
        self.name = 'Apollo'
        self.health = 100
        self.active_weapon = Weapon()

    def attack_dinosaur(self,dinosaur):
        self.active_weapon -= dinosaur.health
        print(f'{dinosaur.health} is the dinosaurs helath')