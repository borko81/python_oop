class Car:

    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return "This is {name} {model} with engine {engine}".format(**self.__dict__)


car = Car("W124", "Mercedes", "Petrol l4")
print(car.get_info())
