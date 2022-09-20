

class Dinosaur:
    def __init__(self) -> None:
        self.name = 'Gasosaurus'
        self.attack_power = 20
        self.health = 100
     


    def attack_robot(self,robot):
        robot.health -= self.attack_power
        print(f'{robot.health} is the Robots health')
    