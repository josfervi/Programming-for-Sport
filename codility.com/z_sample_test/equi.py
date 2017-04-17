def solution(A):
    
    return find_equilibrium_index(nums=A)

def find_equilibrium_index(nums):
    
    """Returns an equilibrium index of nums if one exists. Otherwise returns -1.
    """
    
    N = len(nums)
    
    # For each possible output 0 <= i < N, do two things:
    # 1. Compute pre_sum[i] = sum(nums[:i]) = the sum of everything up to i but not including i
    # 2. Compute post_sum[i] = sum(nums[i+1:]) = the sum of everything after i, but not including i
    # Finally, return i s.t. pre_sum[i] == post_sum[i]. If no such i exists, return -1
    
    pre_sum = [None]*N
    pre_sum_soFar = 0
    
    # INVARIANT:
    #   at the beginning of each iteration
    #   pre_sum_so_Far == sum(nums[:i])
    for i, num in enumerate(nums):
        
        pre_sum[i] = pre_sum_soFar
        pre_sum_soFar += num
    
    post_sum_soFar = 0
    
    # You don't even need list post_sum, you can just use post_sum_soFar.
    
    # INVARIANT:
    #   at the beginning of each iteration
    #   post_sum_soFar == sum(nums[i+1:])
    i = N - 1
    while i >= 0:        
        if pre_sum[i] == post_sum_soFar:
            return i
        
        num = nums[i]
        post_sum_soFar += num
        
        i -= 1
    
    return -1