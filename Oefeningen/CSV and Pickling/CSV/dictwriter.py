
from csv import writer
from csv import DictWriter
from csv import DictReader


with open("cats.csv", "w", newline="") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Age": 10,
        "Breed": "Orange Tabby",
    })


def cm_to_inch(cm):
    return round(float(cm) * 0.393701, 2)


with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_finghters.csv", "w", newline="") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for fighter in fighters:
        height = cm_to_inch(fighter["Height (in cm)"])
        csv_writer.writerow({
            "Name": fighter["Name"],
            "Country": fighter["Country"],
            "Height": height
        })
