
from csv import writer


def add_user(first_name, last_name):
    with open("users.csv", "a", newline="") as file:
        csv_append = writer(file)
        csv_append.writerow([first_name, last_name])


add_user("Dwayne", "Johnson")
