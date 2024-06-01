# Create a function that reverses the string using recursion.

# Write your function here.
def recursive_string(string):
    """
    add the last string to a new variable after removing it from the string, 
    which is immutable...

    base case 
    we've reached index [0]
    """
    if len(string) <=1:
        return string
    # return string[-1] + recursive_string(string[:-1])
    return recursive_string(string[1:]) + string[0]

print(recursive_string("civic")) # civic
print(recursive_string("refer")) # refer
print(recursive_string("string")) # gnirts
print(recursive_string("avocado")) # odacova
print(recursive_string("application")) # noitacilppa


