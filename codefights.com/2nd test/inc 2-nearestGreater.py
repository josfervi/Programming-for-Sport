# fails for large test case
# there must be a better way to do it

def nearestGreater(nums):
    
    n = len(nums)
    
    indeces = [-1] * n
    
    for i, num in enumerate(nums):
        
        max_dist = max(i, n-1-i)
        
        # center myself at i and look
        # at increasingly distant elements
        # of nums for the first one that
        # satisfies the condition
        for d in range(1, max_dist+1):
            
            if i-d >= 0 and nums[i-d] > num:
                indeces[i] = i-d
                break
            
            if i+d < n and nums[i+d] > num:
                indeces[i] = i+d
                break
    
    return indeces
