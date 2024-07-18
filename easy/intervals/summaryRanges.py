def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    # logic: [0,1,2,4,5,7]
    # hold 2 ptrs start, end --> end iterates until it sees something not in range
    # update result list + start, end updated
    
    result = []     # will hold the summary ranges
    if not nums: return result

    start, end = nums[0], nums[0]   

    # loop thru the array
    for i in range(1, len(nums)):
        if nums[i] > end+1:     # if it's > +1 from the current end
            if start != end:
                # add the entire interval
                result.append(str(start) + "->" + str(end))
            else:
                # just add the number by itself
                result.append(str(end))
            # update both the start and end
            start, end = nums[i], nums[i]
        else:
            # just update the end bc it's +1 still 
            end = nums[i]
        
    # doesn't capture the last interval
    if start != end:
        result.append(str(start) + "->" + str(end))
    else:
        result.append(str(end))
    
    return result



