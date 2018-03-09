from random import random

print(flip_coin())


def flip_coin():
    # Generate random number between 0 and 1
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"