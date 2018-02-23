
# for value in range(1, 21):
#     if value == 4 or value == 13:
#         print(f"{value} is unlucky")
#     elif value % 2 == 0:
#         print(f"{value} is even")
#     else:
#         print(f"{value} is odd")

for value in range(1, 21):
    if value == 4 or value == 13:
        state = "unlucky"
    elif value % 2 == 0:
        state = "even"
    else:
        state = "odd"
        
    print(f"{value} is {state}")