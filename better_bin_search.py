# good use of fundamental binary search invariant
# 
# sorted_nums[:l] < target
# sorted_nums[r+1:] > target

def better_bin_search(sorted_nums, target):
    ''' Returns [lower, upper+1] where 
            lower is the index of the first
            occurrence of target in sorted_nums,
            and upper is index of the last
            occurrence of target in sorted_nums.
            If there is no occurrence of target
            in sorted_nums, returns [l,l],
            indicating that no occurrences
            of target exist and that if target
            were to be inserted into sorted_nums,
            it should be inserted in the gap
            between l-1 and l to preserved
            sortedness.
    '''
    
    n = len(sorted_nums)
    
    l, r = 0, n-1
    
    found = None
    
    while l <= r:
        
        mid_idx = (l+r)/2
        mid_val = sorted_nums[mid_idx]
        
        if target < mid_val:
            # look in the left
            r = mid_idx - 1
        
        elif mid_val == target:
            found = mid_idx
            break
        else:
            # look in the right
            l = mid_idx + 1
    
    if not found:
        # return empty range [l, l]
        # signifying target was not
        # found, but if target were
        # to be inserted, it should
        # be inserted in the gap
        # between l-1 and l to
        # preserve sortedness
        return [l, l]
    
    # sorted_nums[:l] < target
    #
    # sorted_nums[l:r+1] contains
    #   an occurrence of target
    #   at sorted_nums[found]
    #   where found == (l+r)/2,
    #   but the rest is unknonw
    #
    # sorted_nums[r+1:] > target
    
    lower, rr = l, r
    while lower <= rr:
        mid_idx = (lower+rr)/2
        mid_val = sorted_nums[mid_idx]
        
        if mid_val < target:
            lower = mid_idx + 1
        else:
            rr = mid_idx - 1
    
    # if lower-1 >= 0, then sorted_nums[lower-1] < target
    # sorted_nums[lower] == target
    
    ll, upper = l, r
    while ll <= upper:
        mid_idx = (ll + upper)/2
        mid_val = sorted_nums[mid_idx]
        
        if mid_val <= target:
            ll = mid_idx + 1
        else:
            upper = mid_idx - 1
    
    # sorted_nums[upper] == target
    # if upper+1 < n, then sorted[upper+1] > target
    
    # sorted_nums[lower:upper+1] == target
    
    return [lower,upper+1]


# Test cases

print better_bin_search([], 1) == [0,0]

print better_bin_search([1,2,3,5,6,7], 4) == [3,3]

print better_bin_search([5,6,7], 4) == [0,0]

print better_bin_search([1,2,3], 4) == [3,3]

print better_bin_search([1,2,3,4,5,6,7], 4) == [3,4]

print better_bin_search([4,4,4,4], 4) == [0,4]

print better_bin_search([1,4,4,4], 4) == [1,4]

print better_bin_search([4,4,4,5], 4) == [0,3]

print better_bin_search([1,2,3,4,4,4,4,5,6,7], 4) == [3,7]