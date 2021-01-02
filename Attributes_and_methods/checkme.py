class Robot:
    __counter = 0

    def __init__(self, name):
        self.name = name
        Robot.__counter += 1

    @staticmethod
    def get_name():
        return Robot.__counter


test = Robot('Test')
print(getattr(test, 'name'))
print(Robot.get_name())