import unittest

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

    def make_order(self):
        PizzaDelivery.ordered = True
        ing = [f'{i}: {k}' for i,k in self.ingredients.items()]
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join(i for i in ing)} and the price will be {self.price}lv.'


class CheckPizza(unittest.TestCase):

    def setUp(self):
        self.p = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})

    def test_params(self):
        PizzaDelivery.ordered = False
        self.assertEqual(self.p.ingredients, {'cheese': 2, 'tomatoes': 1})
        self.assertEqual(self.p.name, 'Margarita')
        self.assertEqual(self.p.price, 11)
        self.assertFalse(PizzaDelivery.ordered, False)

    def test_make_order(self):
        self.p.make_order()
        self.assertTrue(PizzaDelivery.ordered, True)
        ing = [f'{i}: {k}' for i,k in self.p.ingredients.items()]
        self.assertEqual(self.p.make_order(), f'You\'ve ordered pizza {self.p.name} prepared with {", ".join(i for i in ing)} and the price will be {self.p.price}lv.')

    def test_add_ekstra_ing_in_test(self):
        self.p.add_extra('mozzarella', 1, 0.5)
        self.assertEqual(self.p.price, 11.5)
        self.assertEqual(self.p.ingredients, {'cheese': 2, 'tomatoes': 1, 'mozzarella': 1})

    def test_add_ekstra_with_already_order(self):
        self.p.make_order() 
        self.assertEqual(self.p.add_extra('mozzarella', 1, 0.5), f'Pizza {self.p.name} already prepared and we can\'t make any changes!')

    def test_add_ekstra_ing_not_in_test(self):
        self.p.add_extra('cheese', 1, 0.5)
        self.assertEqual(self.p.price, 11.5)
        self.assertEqual(self.p.ingredients, {'cheese': 3, 'tomatoes': 1})

    def test_remove_ingrefdiant_without_already_order(self):
        self.p.remove_ingredient('cheese', 1, 1)
        self.assertEqual(self.p.ingredients, {'cheese': 1, 'tomatoes': 1})

    def test_remove_ingrefdiant_without_already_order_quantiti_is_bigger(self):
        ing = 3
        name = 'cheese'
        self.assertEqual(self.p.remove_ingredient(name, ing, 1), f'Please check again the desired quantity of {name}!')
        self.p.ingredients[name] == 2

if __name__ == '__main__':
    unittest.main()


# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
