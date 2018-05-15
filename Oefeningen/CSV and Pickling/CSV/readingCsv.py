
from csv import reader
from csv import DictReader

# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")


# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     for fighter in data:
#         print(f"{fighter[0]} is from {fighter[1]}")


with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for fighter in csv_reader:
        print(fighter)


