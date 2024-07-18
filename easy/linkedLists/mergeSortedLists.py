def mergeTwoLists(self, list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    
    # logic: keep 2 ptrs, one on list1 and the other on list2
    # as you compare, add node to new LL if <

    list3 = ListNode()
    dummy = list3

    while list1 and list2:
        if list1.val <= list2.val: 
            dummy.next = list1
            list1 = list1.next
        else:
            dummy.next = list2
            list2 = list2.next
        dummy = dummy.next
    
    # if didn't finish list1 or list2... add the following
    while list1: 
        dummy.next = list1
        list1 = list1.next
        dummy = dummy.next
    while list2:
        dummy.next = list2
        list2 = list2.next
        dummy = dummy.next
    
    return list3.next