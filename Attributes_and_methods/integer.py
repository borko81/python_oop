class Integer:

    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return "value is not a float"
        return cls(int(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(value)

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        return self.value + integer.value


first_num = Integer(10)
second_num = Integer.from_float(3.14)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))