def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 1: return False

    # all closing parentheses are in paren_map.values()
    # all starting paren are in paren_map.keys()
    paren_map = {'(':')', '{':'}', '[':']'}

    stack = []

    # loop thru 
    for x in s:
        # if you see a closing bracket...
        if x in paren_map.values():
            # check if it's a mapped pair
            # and check if stack is empty (bc if it's s="}(" that is false)
            if not stack or paren_map[stack.pop()] != x:
                return False
        else: # a starting paren
            stack.append(x)
    
    # only return True if stack is empty
    if not stack: return True
    else: return False