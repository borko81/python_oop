class Shop:

    def __init__(self, name: str, items=None):
        self.name = name
        if items is not None:
            self.items = items
        else:
            self.items = []

    def get_items_count(self):
        return len(self.items)


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())


'''
Create a class called Shop. Upon initialization it should receive a name (string) and items (list). Create a method called get_items_count() which should return the amount of items in the store.
'''
