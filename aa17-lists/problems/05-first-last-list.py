# Create a function that returns the sum of the first value in the first list
# and the last value of the second list.

# Write your function here.
def sum_first_last_list(l1, l2):
    # return (l1[0] + l2[-1])
    sum_list = [l1[0], l2[-1]]
    return sum(sum_list)

print(sum_first_last_list([1, 2, 3], [5, 8, 9]))     #> 10
print(sum_first_last_list([53, 26], [5]))            #> 58
print(sum_first_last_list([9], [5, 8]))              #> 17
print(sum_first_last_list([64], [5, 6, 2]))          #> 66
