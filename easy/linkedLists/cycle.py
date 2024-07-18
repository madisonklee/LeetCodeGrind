def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    # tortoise and hare soln -- fast and slow ptr nodes
    # iterate until fast is Null or fast.next is Null (bc fast increments by 2)
    # if fast == slow then return True (it is a cycle)
    # else return false

    fast = head

    # iterate until fast == None
    while fast and fast.next:
        # update ptrs bc they start at same value already
        head = head.next
        fast = fast.next.next

        # if they ever meet... it's a cycle
        if head is fast:
            return True
    
    return False