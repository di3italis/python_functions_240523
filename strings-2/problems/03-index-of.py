# Create a function that returns the index of a given letter in the string.

# Write your function here.
def index_of(string, b):
    try:
        return string.index(b)
    except ValueError: # will throw VE with out this exception
        return 0


print(index_of("Arm", "a"))  #> 0
print(index_of("Pie", "e"))  #> 2
print(index_of("Lucid", "i"))  #> 3
print(index_of("Obvious","u"))  #> 5
