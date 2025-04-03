class Animal:
    alive = []

    def __init__(self, name, health: int = 100, hidden: bool = False):
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)

    def is_alive(self):
        return self.health > 0

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Carnivore(Animal):
    def bite(self, animal: Animal):
        if self in Animal.alive:
            if isinstance(animal, Herbivore) and animal.hidden:
                print(f"{self.name} cannot bite hidden {animal.name}")
            elif isinstance(animal, Carnivore):
                print(f"{animal.name} is Carnivore, {self.name} cannot bite another Carnivore")
            else:
                animal.health -= 50
                print(f"{self.name} bites {animal.name}! {animal.name}'s health is now {animal.health}")
                if not animal.is_alive():
                    print(f"{animal.name} is dead!")
                    Animal.alive.remove(animal)
        else:
            print(f"{self.name} is dead and cannot bite")

class Herbivore(Animal):
    def hide(self):
        if self in Animal.alive:
            self.hidden = True
            print(f"{self.name} is now hidden")
        else:
            print(f"{self.name} is dead")
