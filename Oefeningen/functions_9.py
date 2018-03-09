
def list_manipulation(itemList, function, location, value = None):
    if function == 'remove' and location == 'end':
        return itemList.pop()
    elif function == 'remove' and location == 'beginning':
        return itemList.pop(0)
    elif function == 'add' and location == 'end':
        itemList.append(value)
        return itemList
    elif function == 'add' and location == 'beginning':
        itemList.insert(0, value)
        return itemList


print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))  # 1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))  # [20,1,2,3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  # [1,2,3,30]
