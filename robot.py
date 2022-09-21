
from weapon import Weapon



class Robot:
    def __init__(self) -> None:
        self.name = 'Apollo'
        self.health = 100
        self.active_weapon = Weapon()
       

    def attack_dinosaur(self,dinosaur):
        dinosaur_health = dinosaur.health - self.active_weapon.attack_power
        print(f'{dinosaur_health} is the dinosaurs health')