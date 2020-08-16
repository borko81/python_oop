def get_sumator():
    result = 0

    def add(x):
        nonlocal result
        result += x
        return result

    return add


def add(x):
    def internal(y):
        return x+ y

    return internal

# summator = get_sumator()
# print(summator(3))
# print(summator(3))
# print(summator(3))

x = add(10)
print(x(20))
