from weapon import Weapon
weapon1 = Weapon()

class Robot:
    def __init__(self) -> None:
        self.name = 'Apollo'
        self.health = 100
        self.active_weapon = weapon1


print(weapon1.attack_power)