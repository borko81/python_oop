class Rombus:

    def __init__(self, number):
        self.number = int(number)

    def hard_code_print(self, i):
        print(' ' * (self.number - i) + '* ' * i)

    def up_romb(self):
        for i in range(1, self.number + 1):
            self.hard_code_print(i)

    def down_romb(self):
        for i in range(self.number - 1, -1, -1):
            self.hard_code_print(i)


# check = Rombus(int(input()))
check = Rombus(3)
check.up_romb()
check.down_romb()