# Problem:
# Given an list of integers, write a method - max_gain -
# that returns the maximum gain.
# Maximum Gain is defined as the maximum difference
# between 2 elements in a list such that the larger element
# appears after the smaller element.
# If no gain is possible, return 0.

# O(n) time
# O(1) extra space
def max_gain(nums):
    
    N = len(nums)
    
    if N < 2:
        return 0
    
    min_so_far= nums[0]
    
    max_gain_so_far= 0
    
    # INVARIANT:
    # at the beggining of each iteration
    #            min_num_so_far  is min( nums[:i-1] )
    #            max_gain_so_far is max_gain( nums[:i] )
    # at the end       of each iteration
    #            min_num_so_far  is min( nums[:i])
    #            max_gain_so_far is max_gain( nums[:i+1] )
    for i in range(1, N):
        min_so_far= min( min_so_far, nums[i-1] )
        max_gain_so_far= max( max_gain_so_far, nums[i] - min_so_far )
    
    return max_gain_so_far