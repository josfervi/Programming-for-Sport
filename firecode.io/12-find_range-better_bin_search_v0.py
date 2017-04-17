def find_range(sorted_nums, target):
    
    low = bin_search_leftmost(sorted_nums, target)
    upper = bin_search_rightmost(sorted_nums, target)
    
    return Range(low, upper-1)

def bin_search_rightmost(sorted_nums, target):
    ''' Returns the index of the rightmost
            occurrence of target in
            sorted_nums. If there is no
            occurrence of target in
            sorted_nums, returns
            the index where target would
            be inserted to preserve
            sortedness.
    '''
    
    n = len(sorted_nums)
    
    l, r = 0, n-1
    
    while l <= r:
        
        mid_idx = (l+r)/2
        mid_val = sorted_nums[mid_idx]
        
        if target < mid_val:
            r = mid_idx - 1
        else:
            l = mid_idx + 1
    
    return l

def bin_search_leftmost(sorted_nums, target):
    ''' Returns the index of the leftmost
            occurrence of target in
            sorted_nums. If there is no
            occurrence of target in
            sorted_nums, returns
            the index where target would
            be inserted to preserve
            sortedness.
    '''
    
    n = len(sorted_nums)
    
    l, r = 0, n-1
    
    while l <= r:
        
        mid_idx = (l+r)/2
        mid_val = sorted_nums[mid_idx]
        
        if target <= mid_val:
            r = mid_idx - 1
        else:
            l = mid_idx + 1
    
    return l
