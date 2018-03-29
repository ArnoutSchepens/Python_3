
def remove_negatives(num_list):
    positive_numbers = list(filter(lambda num: num >= 0, num_list))
    print(positive_numbers)
    return None


remove_negatives([-1, 3, 4, -99])  # [3,4]

remove_negatives([-7, 0, 1, 2, 3, 4, 5])  # [0, 1, 2, 3, 4, 5]

remove_negatives([50, 60, 70])  # [50,60,70]
