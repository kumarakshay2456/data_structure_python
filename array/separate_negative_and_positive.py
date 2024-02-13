"""
Prob- you-are-given-an-array-arr-consisting-of-n-integers-you-need-to-rearrange-the-array-elements-such-that-
        all-negative-numbers-appear-before-all-positive-numbers"
Time complexity: O(N)
Space Complexity: O(1)
Where N is the number of elements in the array.

"""


def separateNegativeAndPositive(nums):

    # Create two pointers- "LEFT" and "RIGHT"
    left = 0
    right = len(nums) - 1

    while left < right:

        if nums[left] < 0 and nums[right] < 0:
            # Case 1: Both the pointers point to negative elements.
            left += 1

        elif nums[left] >= 0 and nums[right] >= 0:
            # Case 2: Both the pointers point to positive elements.
            right -= 1

        elif nums[left] >= 0 and nums[right] < 0:
            # Case 3: "LEFT" points to positive element and "RIGHT" points to negative element.
            get = nums[left], nums[right]
            nums[right], nums[left] = get
            left += 1
            right -= 1

        else:
            # Case 4: "LEFT" points to negative element and "RIGHT" points to positive element.
            left += 1
            right -= 1

    return nums
