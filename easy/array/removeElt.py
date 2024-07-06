# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

def removeElement(nums, val):
    # define 2 ptrs, 1 at start, 1 at end
    p = 0
    pEnd = len(nums) - 1
    k=0

    while p<pEnd:
        if nums[p] == val:
            # perform swap
            temp = nums[pEnd]
            nums[pEnd] = nums[p]
            nums[p] = temp

            pEnd-=1
            if nums[p] != val: p+=1
        else:
            p+=1
    
    # get k value: count until hit val
    for x in nums:
        if x == val: break
        k+=1
                
    return k

nums = [3,2,2,3]
val = 3
k = removeElement(nums, val)

print(nums[0:k])