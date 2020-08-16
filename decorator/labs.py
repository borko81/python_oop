# 1
# def number_increment(numbers):
#     def increase():
#         return list(map(lambda x: x+1, numbers))
#
#     return increase()
#
#
# print(number_increment([1,2,3]))

# 2
# def vowel_filter(function):
#     def wrapper():
#         result = function()
#         vowels = ['a', 'o', 'u', 'y', 'i', 'e']
#         return [x for x in result if x in vowels]
#
#     return wrapper
#
#
# @vowel_filter
# def get_letter():
#     return ['a', 'b', 'c', 'd', 'e']
#
#
# print(get_letter())

# 3
# def even_numbers(function):
#     def wrapper(numbers):
#         return [x for x in numbers if x % 2 == 0]
#
#     return wrapper
#
#
# @even_numbers
# def get_numbers(numbers):
#     return numbers
#
# print(get_numbers([1, 2, 3, 4, 5]))

# 4
from functools import wraps


def multiply(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))




































