
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 1),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }

    is_float = kwargs.get('make_float', False)

    operation_value = operation_lookup[kwargs.get('operation', '')]

    if is_float:
        final = "{} {}".format(kwargs.get(
            'message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get(
            'message', 'the result is'), int(operation_value))
    return final


# print(calculate(make_float=False, operation='add', message='You just added',
#                first=2, second=4))
# "You just added 6"
# print(calculate(make_float=True, operation='divide',
#                first=3.5, second=5))
# "The result is 0.7"

def greet_boss(employee = None, boss = None):
    print(f"{employee} greets {boss}")

names = {"boss": "Bob", "employee": "Colt"}
greet_boss()
greet_boss(**names)

cube = lambda num: num**3
print(cube(2))
print(cube(3))
print(cube(8))