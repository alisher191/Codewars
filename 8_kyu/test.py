"""8. Напишите функцию, которая возвращает рандомное число, а затем декоратор
который делит это число на 2."""

#
def decor(function):
    def wrapper(*args):
        print(function() / 2)
    return wrapper


import random
@decor
def give_back():
    b = (random.randint(1, 100))
    return b  #f'It is a random number: {b}'

give_back()
