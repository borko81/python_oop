class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))


'''
Create a class called Hero. Upon initialization it should receive a name (string) and health (number). Create two functions:
- defend(damage) - Deal the given damage to the hero; if the health is 0 or less, set it to 0 and return "{name} was defeated".
- heal(amount) - Increase the health of the hero with the given amount.

'''
