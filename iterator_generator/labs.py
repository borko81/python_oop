# class custom_range:
#     def __init__(self, start, end):
#         self.end = end
#         self.start = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.start
#         if self.start <= self.end:
#             self.start += 1
#             return temp
#         raise StopIteration()
#
#
# one_to_ten = custom_range(1, 10)
# for num in one_to_ten:
#     print(num)

# 02. Reverse Iter

# class reverse_iter:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.n = len(iterable) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.n
#         if self.n >= 0:
#             self.n -= 1
#             return self.iterable[temp]
#         raise StopIteration()
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)

# 03. Vowels

# class vowels:
#     def __init__(self, string):
#         self.string = string
#         self.vowels = ['a', 'e', 'y', 'o', 'u', 'i']
#         self.end = len(string) - 1
#         self.begin = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.begin
#         if self.begin <= self.end:
#             self.begin += 1
#             if self.string[temp].lower() in self.vowels:
#                 return self.string[temp]
#             else:
#                 return self.__next__()
#         raise StopIteration()
#
#
# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)

# 04. Squares

# def squares(n):
#     return ((m**2  for m in range(1, n + 1)))
#
# print(list(squares(5)))

# 05. Generator Range
# def genrange(start, end):
#     while start <= end:
#         yield start
#         start += 1
#
# print(list(genrange(1, 10)))

# 06. Reverse string
def reverse_text(string):
    l = len(string) - 1
    while l >= 0:
        yield string[l]
        l -= 1


for char in reverse_text("step"):
    print(char, end='')

























