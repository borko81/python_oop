class Tiger:

    def __init__(self, name, gender, age):
        self.age = age
        self.name = name
        self.gender = gender

    @staticmethod
    def get_needs():
        return 45

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'