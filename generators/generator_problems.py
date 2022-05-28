import random

def gensquares(n):
    for i in range(n):
        yield i ** 2

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)
