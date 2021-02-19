class Hero:

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def check_health_is_less_then_zero(self):
        return self.health <= 0

    def defend(self, demage: int):
        self.health -= demage
        if self.check_health_is_less_then_zero():
            self.health = 0
            return "%s was defeated" % self.name

    def heal(self, amount: int):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
