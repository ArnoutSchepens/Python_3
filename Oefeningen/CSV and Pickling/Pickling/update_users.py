
from csv import reader, writer


def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
    with open("users.csv") as file:
        rows = list(reader(file))

    count = 0
    with open("users.csv", "w", newline="") as file:
        csv_writer = writer(file)
        for row in rows:
            match_first_name = row[0] == old_first_name
            match_last_name = row[1] == old_last_name
            if match_first_name and match_last_name:
                csv_writer.writerow([new_first_name, new_last_name])
                count += 1
            else:
                csv_writer.writerow(row)
    return count

print(update_users("Colt", "Steele", "Dewi", "Goossens"))
