'''
State monitoring
'''

class Invetory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        '''Attach observ to list with observers'''
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        '''Run observer after any change'''
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, invertory):
        self.inventory = invertory

    def __call__(self, *args, **kwargs):
        data = {
            "product": self.inventory.product,
            "quantity": self.inventory.quantity
        }
        print(data)


if __name__ == '__main__':
    i = Invetory()
    c = ConsoleObserver(i)
    i.attach(c)
    i.product = 'Widget'
    print(i.product)
    i.product = 'New Widget'