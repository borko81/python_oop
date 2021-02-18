class Flower:

    def __init__(self, name: str, water_requirements, is_happy=False):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = is_happy

    def mycheck_is_happy(self, quantity):
        return quantity >= self.water_requirements

    def water(self, quantity):
        self.is_happy = self.mycheck_is_happy(quantity)

    def status(self):
        return f"{self.name} is happy" if self.is_happy else f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
