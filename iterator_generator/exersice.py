# 01. Take Skip

# class take_skip:
#
#     def __init__(self, step, count):
#         self.count = count
#         self.step = step
#         self.r = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.r
#         if self.r < self.count:
#             self.r += 1
#             return temp * self.step
#         raise StopIteration()
#
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)

# 02. Dictionary Iterator
# class dictionary_iter:
#     def __init__(self, dict):
#         self.dict = dict
#         self.length = len(self.dict)
#         self.keys = list(self.dict.keys())
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.length:
#             key = self.keys[self.current]
#             val = self.dict[key]
#             self.current += 1
#             return (key, val)
#         raise StopIteration()
#
#
#
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)

# 03. Countdown Iterator
# class countdown_iterator:
#     def __init__(self, count):
#         self.count = count
#         self.begin = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.count
#         if self.count >= 0:
#             self.count -= 1
#             return temp
#         raise StopIteration()
#
#
# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")

# 04. Sequence Repeat
# class sequence_repeat:
#
#     def __init__(self, sequence, number):
#         self.number = number
#         self.sequence = sequence
#         self.current_index = 0
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter < self.number:
#             if self.current_index == len(self.sequence):
#                 self.current_index = 0
#             self.current_index += 1
#             self.counter += 1
#             return self.sequence[self.current_index - 1]
#         raise StopIteration()
#
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')

# 05. Take Halves
# def solution():
#     def integers():
#         begin = 1
#         while True:
#             yield begin
#             begin += 1
#
#     def halves():
#         for i in integers():
#             yield i / 2
#
#     def take(n, seq):
#         count = 0
#         my_list = []
#         for num in seq:
#             if count == n:
#                 return my_list
#             else:
#                 my_list.append(num)
#             count += 1
#
#     return (take, halves, integers)
#
#
# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))

# 06. Fibonacci Generator
# def fibonacci():
#     current_num = 1
#     previous = 0
#     while True:
#         yield previous
#         previous, current_num = current_num, previous + current_num
#
#
#
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))

# 07. Reader
# def read_next(*args):
#     for element in args:
#         for e in element:
#             yield str(e)
#
# for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
#     print(item, end='')

# 08. Prime Numbers
# def get_primes(integers):
#     for i in integers:
#         if i < 2:
#             continue
#         is_prime = True
#         for num in range(2, i):
#             if i % num == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield i
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# 09. Possible permutations
# from itertools import permutations
#
# def possible_permutations(item):
#     for per in permutations(item):
#         yield list(per)
#
# [print(n) for n in possible_permutations([1, 2, 3])]






















































