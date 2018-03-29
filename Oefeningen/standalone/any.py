
def is_all_strings(list_items):
    return all((isinstance(x, str) for x in list_items))

print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2, 'a', 'b', 'c']))
print(is_all_strings(['hello', 'goodbye']))