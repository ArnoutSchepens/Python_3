
password = "stop copying me"
text = input('Say something: ')
while text.lower() != password:
    # print(text)
    # text = input()
    # Much shorter, but less clear
    text = input(f"{text}\n")

print("OK, you win!")