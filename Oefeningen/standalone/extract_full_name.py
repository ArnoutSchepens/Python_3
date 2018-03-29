
import pdb



def extract_full_name(list_items):
    # return [item["first"] + " " + item["last"] for item in list_items]
    return [f"{item['first']} {item['last']}" for item in list_items]
    
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']