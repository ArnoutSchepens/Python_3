
numbers_1 = [1, 2, 3, 4]
numbers_2 = [3, 4, 5, 6]
answer = [number for number in numbers_1 if number in numbers_2]
print(answer)

friends = ['Elie', 'Colt', 'Matt']
answer2 = [friend.lower()[::-1] for friend in friends]
print(answer2)