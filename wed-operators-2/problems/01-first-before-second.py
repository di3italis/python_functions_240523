# You are given three inputs: a string, one letter, and a second letter.

# Write a function that returns `True` if every instance of the first letter
# occurs before every instance of the second letter.

# Look at the String Methods to possibly help you find some methods that can
# make this easier.
# https://docs.python.org/3.9/library/stdtypes.html?highlight=strings#string-methods
# str.rfind(sub[, start[, end]])
# Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.
# str.find(sub[, start[, end]])
# Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

# Write your function here.
def first_before_second(s, a, b):
    # collect indices of a and b
    a_list = []
    b_list = []
    # iterate through the string
    for i in range(len(s)):
        if s[i] == a:
            a_list.append(i)
        if s[i] == b:
            b_list.append(i)
    # check if a comes before b
    for a in a_list:
        for b in b_list:
            if a > b:
                return False
    return True

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

# Path: 02-second-before-first.py
# a and b could also just hold the last index occurance of a and b
# loop str and update indices of a and b
# and then check if a > b
# if yes return False
# else return True
#
# def first_before_second(s, a, b):
#     # collect indices of a and b
#     a_index = -1
#     b_index = -1
#     # iterate through the string
#     for i in range(len(s)):
#         if s[i] == a:
#             a_index = i
#         if s[i] == b:
#             b_index = i
#         if a_index > b_index:
#             return False
#     return True

#another option:
# def first_before_second(s, a, b):
#     # Collect indices of occurrences of 'a' and 'b'
#     a_list = [i for i in range(len(s)) if s[i] == a]
#     b_list = [i for i in range(len(s)) if s[i] == b]
#     
#     # Ensure all indices of 'a' are before any index of 'b'
#     for a_index in a_list:
#         for b_index in b_list:
#             if a_index > b_index:
#                 return False
#     return True
#
# # Test cases
# print(first_before_second("a rabbit jumps joyfully", "a", "j"))  # True
# print(first_before_second("knaves knew about waterfalls", "k", "w"))  # True
# print(first_before_second("happy birthday", "a", "y"))  # False
# print(first_before_second("precarious kangaroos", "k", "a"))  # False
#
