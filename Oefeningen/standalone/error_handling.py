
# import random
# import random as omg_so_random
# from random import *
# from random import choice, shuffle
from random import choice as ch, randint as rInt

def divide(num1, num2):
    try:
        res = num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    else:
        return res


print(divide(4,2))  # 2
print(divide([],"1"))  # "Please provide two integers or floats"
print(divide(1,0))  # "Please do not divide by zero"