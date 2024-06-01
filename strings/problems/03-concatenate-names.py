# Given two strings, `first_name` and `last_name`, return a single string in the
# format "last, first".

# Write your function here.
def concat_name(a, b):
    return '"' + b + ', ' + a + '"'


print(concat_name("First", "Last"))  #> "Last, First"
print(concat_name("John", "Doe"))    #> "Doe, John"
print(concat_name("Mary", "Jane"))   #> "Jane, Mary"

