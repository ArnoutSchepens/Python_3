
def sum_odd_numbers(numbers):
    total = 0
    odd_numbers = [num for num in numbers if num % 2 == 0]
    for num in odd_numbers:
        total += num
    return total


sum_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
