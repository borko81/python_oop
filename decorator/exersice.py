# 7 Execution time
# from timeit import default_timer as timer
#
#
# def exec_time(func):
#     def wrapper(*args):
#         t1 = timer()
#         func(*args)
#         end = timer()
#         return end - t1
#     return wrapper
#
#
# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
#
# print(loop(1, 10000000))

# 8 Store results
# class store_results:
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, *args, **kwargs):
#         with open('results.txt', 'a') as f:
#             result = self._func(*args, **kwargs)
#             f.write(f'Function {self._func.__name__} was add called. Result: {result}\n')
#
#
#
# @store_results
# def add(a, b):
#     return a + b
#
# @store_results
# def mult(a, b):
#     return a * b
#
# add(2, 2)
# mult(6, 4)

# 5 Cache
# def cache(func):
#     def wrapper(n):
#         result = func(n)
#         wrapper.log[n] = result
#         return result
#     wrapper.log = {}
#     return wrapper
#
# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# fibonacci(3)
# print(fibonacci.log)

# 1 Logger
# def logged(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args)
#         return f'you called {func.__name__}{args}\nit returned {result}'
#     return wrapper
#
#
# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))

# 3 Bold, Italic, Underline
# def make_bold(func):
#     def wrapper(*args):
#         return f'<b>{func(*args)}</b>'
#     return wrapper
#
#
# def make_italic(func):
#     def wrapper(*args):
#         return f'<i>{func(*args)}</i>'
#     return wrapper
#
#
# def make_underline(func):
#     def wrapper(*args):
#         return f'<u>{func(*args)}</u>'
#     return wrapper
#
#
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f'Hello, {name}'
#
# print(greet('Peter'))

# 4 Type Check
# def type_check(type):
#     def decorator(func):
#         def wrapper(n):
#             if isinstance(n, type):
#                 return func(n)
#             return "Bad Type"
#         return wrapper
#     return decorator
#
#
# @type_check(int)
# def times2(num):
#     return num * 2
#
# print(times2(2))
# print(times2('Not a number'))

# 6 HTML Tag
# def tags(p):
#     def decorator(func):
#         def wrapper(*args):
#             result = func(*args)
#             return f'<{p}>{result}</{p}>'
#         return wrapper
#     return decorator
#
#
# @tags('h1')
# def to_upper(text):
#     return text.upper()
# print(to_upper('hello'))

# 02. Even Parameters
def even_parameters(func):
    def wrapper(*args):
        if any(isinstance(i, str) for i in args):
            return 'Please use only even numbers!'
        elif all(i % 2 == 0 for i in args):
            return func(*args)
        else:
            return 'Please use only even numbers!'
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
print('-' * 10)
@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))




















