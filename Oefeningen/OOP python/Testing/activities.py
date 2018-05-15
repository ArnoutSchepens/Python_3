
from random import choice


def eat(food, is_healty):
    if not isinstance(is_healty, bool):
        raise ValueError

    ending = "because YOLO"

    if is_healty:
        ending = "because my body is a temple"

    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours < 2:
        return f"I slept enough. That felt great!"

    return f"I slept too long!"


def is_funny(person):
    if person is "Tim":
        return False

    return True


def laugh():
    return choice(("Lol", "Haha", "Tehehe"))
