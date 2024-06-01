# Declare a variable that contains a string. Then try to change the first letter
# of the string and `print` your string.

# Write your function here.
str = "my_string"
def immut_str(str):
    str[0] = "x"
    return str

print(immut_str(str))

def mut_str(str):
    x_first = "x"
    return x_first + str[1:]

print(mut_str(str))
