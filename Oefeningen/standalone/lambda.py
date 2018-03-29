
def decrement_list(num_list):
    return list(map(lambda num: num - 1, num_list))


print(decrement_list([1, 2, 3]))
print(decrement_list([20, 14, 11]))


names = ["austin", "Penny", "Anthony", "Angel", "Billy"]
print(list(filter(lambda name: name[0].upper() == "A", names)))