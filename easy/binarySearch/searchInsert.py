# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

def binary_search(arr, low, high, x):

    # check the base case
    if high >= low:
        mid = (high + low) // 2
        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only be present in LEFT subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        
        # else elt can only be present in RIGHT subarray
        else:
            return binary_search(arr, mid+1, high, x)

    else:
        # Element is not present in the array
        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = binary_search(arr, 0, len(arr)-1, x)
print(str(result))




# BINARY SEARCH NOTES: 
# given sorted arr, highest elt, lowest elt, and target
# if target is in arr, return index
# if target is not in arr, return -1

# nums is an arr, target is an int
def searchInsert(nums, target):
    # first pass
    high = len(nums)-1
    low = 0
    
    # call actual binarysearch in this func
    def binarysearch(arr, target, high, low):
        if high >= low:
            # find midpoint
            mid = (high+low)//2
            



        else: 
            return -1 


    resultIndex = binary_search(nums, target, high, low)
