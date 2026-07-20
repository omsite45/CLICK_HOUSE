import random

def random_price(low, high):

    return round(random.uniform(low, high), 2)


def random_discount():

    return random.choice([0, 5, 10, 15, 20, 25])


def random_rating():

    return round(random.uniform(1, 5), 1)