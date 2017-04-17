# https://www.interviewbit.com/problems/rotated-array/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, nums):
        
        n= len(nums)
        
        if n == 0:
            return None
        
        last= nums[-1]
        
        lo= 0
        while lo < n-1 and nums[lo] == last:
            lo+= 1
            
        # {nums[:lo] == last}
        
        hi= n - 1
        
        while lo <= hi:
            
            mid_idx = (lo+hi)/2
            mid_val = nums[mid_idx]
            
            if mid_val > last:
                
                # we know that everything > last
                # has to be in the bigger sorted sublist which is on the left
                lo= mid_idx + 1
            
            elif mid_val <= last:
                # we know everything < last
                # has to be in the smaller sorted sublist which is on the right
                # because of lns 13-15
                # we also know everything = last
                # also has to be in the smaller sorted sublist too
                hi= mid_idx - 1
        
        return nums[lo]