import random


def suma(x, y):
    return x + y

def diff(x, y):
    return x - y

def div(x, y):
    return x / y

def mn(x, y):
    return x * y


def rand():
    return random.randint(1, 10)

def suma_with_rand(x, y):
    r = rand()
    return x + y + r