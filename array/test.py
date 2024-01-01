
def removeElement(nums = [3,3], val = 3):
    l = 2
    count = 0
    for i in range(l):
        if val == nums[i]:
            count += 1
            while nums[l - count] == val:
                nums[l - count] = "_"
                count += 1
                i+=1
            if l - count == 0:
                nums[l - count] = "_"
                     # Starting point the
            else:
                p = nums[l - count]
                nums[l - count] = '_'
                nums[i] = p
    print(nums, count)
    return l - count if l - count > 0 else -1


print(removeElement())