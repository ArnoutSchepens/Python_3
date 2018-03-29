
def is_palindrome(string):
    # char_list = [char for char in string.lower() if char != ' ']
    # string = ''.join(char_list)
    stripped = string.replace(' ','').lower()
    return stripped == stripped[::-1]

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama')) # True
print(is_palindrome('a man a plan a canal Panama')) # True