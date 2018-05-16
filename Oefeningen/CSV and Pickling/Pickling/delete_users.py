

from csv import reader, writer

def delete_users(first_name, last_name):
    count = 0

    with open("users.csv") as file:
        csv_list = list(reader(file))
    
    with open("users.csv", "w", newline="") as file:
        csv_writer = writer(file)
        for row in csv_list:
            first_name_match = row[0] == first_name
            last_name_match = row[1] == last_name
            if first_name_match and last_name_match:
                count += 1
            else:
                csv_writer.writerow(row)
            
    return count


print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele"))
print(delete_users("Not", "Here"))