
def triple_and_filter(list_item):
    return [item * 3 for item in list_item if item % 4 == 0]
    # return list(filter(lambda x: x % 4 == 0, map(lambda x: x * 3, list_item)))

print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]
