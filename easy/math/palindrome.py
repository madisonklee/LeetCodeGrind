# Given an integer x, return true if x is a palindrome, and false otherwise.
# Input: x = 121
# Output: true


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    stringVersion = str(x)

    # declare ptrs, at start and end
    start = 0
    end = len(stringVersion)-1

    while start<end:
        if stringVersion[start] != stringVersion[end]:
            return False
        start+=1
        end-=1
    
    return True

print(isPalindrome(x = 121))
