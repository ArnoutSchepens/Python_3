
def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day



# days = week()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))


def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


gen = yes_or_no()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))