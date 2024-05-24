# Recall the merge sort algorithm:

# 1. Find midpoint to divide list in half
# 2. Call `merge_sort` recursively on the first half
# 3. Call `merge_sort` recursively on the second half
# 4. Merge the two sorted halves with `merge`

# Implement the `merge_sort` function with the `merge` helper function.

# Write your code here.
def merge_sort(lst):
    # Call merge somewhere in here
    # return lst.sort()
    l = len(lst);

    if l == 0 or l == 1:
        return lst

    mid = l // 2;
    print('calling merge sort on split list right:',  lst[0:mid])
    print('calling merge sort on split list left:',  lst[mid:])
    right_list = merge_sort(lst[0:mid])
    left_list = merge_sort(lst[mid:])
    # print(right_list)
    # print(left_list)
    return merge(right_list, left_list)

# def merge(first_half, second_half):
#     # Merge logic goes here
#     pass

def merge(left, right):
    # return
    #want to return a merge of the 2 items.
    #if it is only 1 item each just compare 1 item.
    print('merging', left, 'and', right)
    result = []
    while len(left) > 0 and len(right) > 0:
      if left[0] < right[0]:
        result.append(left[0])
        left = left[1:]
      else:
        result.append(right[0])
        right = right[1:]

    if len(left):
        result += left[::]

    if len(right):
        result += right[::]

    return result
lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
# print(sorted_lst)

# merge_sort(lst)                     # In place solution
# print(lst)
