# Create a function that returns whether or not the string is a Palindrome.

# Write your function here.
def is_palindrome(string):
    return string[::-1] == string[0:]

print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False

# slicing backwards
#! [start:end:step]
#! [::-1] reverse slice
# string = "Hello"
# string[::-1] == "olleH"

