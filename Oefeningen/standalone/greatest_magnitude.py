def max_magnitude(list_items):
    return max([abs(item) for item in list_items])

print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))



def sum_even_values(*args):
    return sum([item for item in args if item % 2 == 0])

print(sum_even_values(1,2,3,4,5,6)) # 12
print(sum_even_values(4,2,1,10)) # 16
print(sum_even_values(1)) # 0



def sum_floats(*args):
    return sum([item for item in args if isinstance(item, float)])
    # return isinstance()


print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
print(sum_floats(1,2,3,4,5)) # 0