class PizzaDelivery:
    ordered = False
    
    def __init__(self, name: str, price: float, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f'Pizza {self.name} already prepared and we can\'t make any changes!'

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price
            
        else:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f'Pizza {self.name} already prepared and we can\'t make any changes!'

        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'

        elif self.ingredients[ingredient] < quantity:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price

    def pizza_ordered(self):
        PizzaDelivery.ordered = True
        ing = [f'{i}: {k}' for i,k in self.ingredients.items()]
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join(i for i in ing)} and the price will be {self.price}lv.'