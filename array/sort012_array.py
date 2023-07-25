"""
you-have-been-given-an-integer-array-list-arr-of-size-n-it-only-contains-0s-1s-and-2s-write-a-solution-to-sort-this-array-list
"""


def sort012(arr, n):
    # write your code here
    # don't return anything
    count_0, count_1, count_2 = 0, 0, 0
    for arr_value in arr:
        if arr_value == 0:
            count_0 += 1
        elif arr_value == 1:
            count_1 += 1
        elif arr_value == 2:
            count_2 += 1
    i = 0
    while i <= count_0 + count_1 + count_2:
        if i < count_0:
            arr[i] = 0
        elif i < count_0 + count_1:
            arr[i] = 1
        elif i < count_0 + count_1 + count_2:
            arr[i] = 2
        i += 1
    return arr
