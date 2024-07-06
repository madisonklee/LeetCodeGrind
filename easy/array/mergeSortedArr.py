# merge 2 sorted arrays - Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]     -> must be stored in nums1

# SOLN: hav 3 ptrs, at m-1, n-1, and len(nums1)-1
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

def merge(nums1, m, nums2, n):
    ptr1 = m - 1
    ptr2 = n - 1
    p = len(nums1) - 1

    while ptr2 > -1:
        if nums1[ptr1] > nums2[ptr2]:
            nums1[p] = nums1[ptr1]
            ptr1 -= 1
        else: 
            nums1[p] = nums2[ptr2]
            ptr2 -= 1
        p-=1
    
    while ptr2 > -1:
        nums1[p] = nums2[ptr2]

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3
merge(nums1, m, nums2, n)
print(nums1)
