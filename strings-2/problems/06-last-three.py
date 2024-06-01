# Create a function that returns a boolean indicating whether the last three
# letters of the string match the given letters (regardless of the letter's
# case).

# Write your function here.
def last_three(a, b):
    a = a.lower()
    b = b.lower()
    last3 = a[-3:]
    # print(a, b, las)
    return last3 == b



print(last_three("Power", "wer"))  #> True
print(last_three("Application", "App"))   #> False
print(last_three("Raw", "raw"))   #> True
print(last_three("Bonjour", "OUR"))   #> True
