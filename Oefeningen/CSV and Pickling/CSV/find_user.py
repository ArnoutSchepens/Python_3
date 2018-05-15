
from csv import DictReader

def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        for idx, user in enumerate(csv_reader):
            first_name_match = user['First Name'] == first_name
            last_name_match = user['Last Name'] == last_name
            if first_name_match and last_name_match:
                return idx
        return "User was not find"


print(find_user("Alan", "Turing"))