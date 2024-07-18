# what is binary search?
# given sorted array, target, the high and low ptrs
# find the midpoint
# if target == mid --> return mid as found
# if target > mid --> go to upper half of arr
# else if target < mid --> go to lower half

def binarySearch(arr, target, low, high):
    if low<high:
        mid = (low + high)//2
        if arr[mid] == target: return mid
        elif target>arr[mid]: binarySearch(arr, target, mid+1, high)
        else: binarySearch(arr, target, low, mid-1)
    else:
        return -1

target = 4
arr = [1,2,3,4,5,6,7,8]

print(binarySearch(arr, target, 0, len(arr) - 1))