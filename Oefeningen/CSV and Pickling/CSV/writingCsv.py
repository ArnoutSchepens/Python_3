
from csv import writer
from csv import reader

with open("cats.csv", "w", newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Race"])
    csv_writer.writerow(["Vlootje", "Maine Coon"])
    csv_writer.writerow(["Poukie", "Neva Masequerade"])


with open("fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]

with open("screaming_fighters.csv", "w", newline='') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)