import random

fruit_name = 'apple'


def harvest():
    return [fruit_name] * random.randint(1, 9)
