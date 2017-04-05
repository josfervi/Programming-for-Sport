# https://www.interviewbit.com/problems/length-of-longest-subsequence/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    
    # O(nlgn) time
    def longestSubsequenceLength(self, nums):
        
        # dp_len_inc[i] means we can achieve
        # a strictly increasing subsequence
        # of length dp_len_inc[i] with a tail
        # of nums[i] using the items in nums[:i+1]
        dp_len_inc = self.get_dp_len(nums) # O(nlgn)
        
        # dp_len_dec[i] means we can achieve
        # a striclty decreasing subsequence
        # of length dp_len_dec[i] with a head
        # of nums[i] using the items in nums[i:]
        dp_len_dec = list(reversed(self.get_dp_len(list(reversed(nums))))) # O(nlgn)
        
        max_len_soFar = 0
        
        for len_inc, len_dec in zip(dp_len_inc, dp_len_dec):
            
            max_len_soFar = max(max_len_soFar, len_inc + len_dec - 1)
        
        return max_len_soFar
    
        
    def get_dp_len(self, nums):
        
        n = len(nums)
        
        # dp_min[i] means that we can achieve
        # a strictly increasing subsequence
        # of lenght i with a tail of dp_min[i]
        dp_min = [None]
        
        # dp_len[i] means that we can achieve
        # a strictly increasing subsequence
        # of length dp_len[i] with a tail of
        # nums[i]
        dp_len = [None]*n
        
        for i, num in enumerate(nums):
            
            # desired result:
            #                 r l
            # dp_min = [ < num | >= num ]
            
            l,r = my_bisect_left(dp_min, num, l=1, r=len(dp_min)-1)
            
            if l >= len(dp_min):
                dp_min.append(num)
            else:
                dp_min[l] = num
            
            dp_len[i] = l
        
        return dp_len


def my_bisect_left(nums, target, l=0, r=None):
    
    # desired result:
    #     r l
    # [ <t | >=t ]
    
    if not None:
        r = len(nums)-1
    
    while l<=r:
        
        mid_idx = (l+r)/2
        mid_val = nums[mid_idx]
        
        if mid_val < target:
            l = mid_idx + 1
        else:
            r = mid_idx - 1
    
    return l,r
