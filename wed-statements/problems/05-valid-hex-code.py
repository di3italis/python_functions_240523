# Create a function that determines whether a string is a valid hex code.

# A hex code must begin with a pound key # and is exactly 6 characters in
# length. Each character must be a digit from 0-9 or an alphabetic character
# from A-F. All alphabetic characters may be uppercase or lowercase.

# Write your function here.
# start with #
# str has 6 char
# each char 0-9 or a-f

def is_valid_hex_code(code):
    # alan solution:
    postHash = code[1:]
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f']

    if code[0] != "#":
        return False
    if len(postHash) != 6 or not postHash.isalnum():
        return False

    for char in postHash:
        if char.lower() not in valid_letters and not char.isdigit():
            return False
    return True

# my attempt:
    # if code[0] != "#":
    #     return False
    # code = code[1:]
    # alnum_chk = code.isalnum()
    # len_chk = len(code) == 6
    # if not (alnum_chk and len_chk):
    #     return False
    # for i in code:
    #     print(i)
    #     if i.isalpha() and i.lower() < "g":
    #         return True


print(is_valid_hex_code("#CD5C5C"))  #> True
print(is_valid_hex_code("#EAECEE"))  #> True
print(is_valid_hex_code("#eaecee"))  #> True

print(is_valid_hex_code("#CD5C58C"))
# Prints False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z"))
# Prints False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C"))
# Prints false
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C"))
# Prints False
# Missing #
