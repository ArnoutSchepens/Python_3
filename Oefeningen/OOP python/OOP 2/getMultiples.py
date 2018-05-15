
# def get_multiples(number = 1, count = 10):
#     for num in range(1, count + 1):
#         yield number * num



# evens = get_multiples(2, 3)
# print(next(evens)) # 2
# print(next(evens)) # 4
# print(next(evens)) # 6
# # next(evens) # StopIteration

# default_multiples = get_multiples()
# print(list(default_multiples)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_unlimited_multiples(number = 1):
    res = number
    while True:
        yield res
        res += number


sevens = get_unlimited_multiples(7)
[print(next(sevens)) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[print(next(ones)) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]