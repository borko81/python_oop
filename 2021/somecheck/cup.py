class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        temp = self.quantity + milliliters
        if self.size >= temp:
            self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


# May has condition without fill the cup
cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())
