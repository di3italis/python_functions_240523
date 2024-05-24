# It's time to explore the *list* object and how to use it Follow the
# instructions in the code comments. Be sure to test your work by running your
# code!

# DO NOT EDIT - Starting with a simple lists of colors and numbers
colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
numbers = [2, 34, 8.5, -22.0, 33//4, 2**5]
print ('COLORS', colors)
print ('NUMBERS', numbers)

# 1. Print the total number of colors (length of the list)
print(len(colors))
# 2. Print the first color
print(colors[0])

# 3. Print the second and third colors
print(colors[1:3])

# 4. Print the last two colors
print(colors[-2:])

# 5. Print the smallest number in the numbers list
print( min(numbers))

# 6. Print the largest number in the numbers list
print( max(numbers))

# UNCOMMENT WHEN YOU WORK ON #7
numbers.sort()

print ('SORTED NUMBERS', numbers)

# 8. Sort the colors alphabetically ignoring case

# UNCOMMENT WHEN YOU WORK ON #8
colors2 = []
for i in colors:
  colors2.append(i.lower())
colors2.sort()


# def my_sort(x):
#   return x.lower()

# colors.sort(key=my_sort)
colors.sort(key=lambda x: x.lower())
# colors.sort()


print ('SORTED COLORS', colors)
