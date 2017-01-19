# https://www.interviewbit.com/problems/count-element-occurence/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    
    # O(lgn) time
    # O(1)   working space
    def findCount(self, nums, target):
        
        first_idx= self.bin_search_w_firstFlag(nums, target, firstFlag= True)
        
        if first_idx == -1:
            return 0
        
        last_idx= self.bin_search_w_firstFlag(nums, target, firstFlag= False)
        
        return last_idx - first_idx + 1
    
    def bin_search_w_firstFlag(self, nums, target, firstFlag):
        
        lo, hi = 0, len(nums) - 1
        
        res= -1
        
        while lo <= hi:
            
            mid_idx= (lo+hi)/2
            mid_val= nums[mid_idx]
            
            if mid_val == target:
                
                res= mid_idx
                
                if firstFlag:
                    # look for first idx of target in left half
                    hi= mid_idx - 1
                else:
                    # look for last idx of target in right half
                    lo= mid_idx + 1
            
            elif target < mid_val:
                # look for target in left half
                hi= mid_idx - 1
            else: # target > mid_val
                # look for target in right half
                lo= mid_idx + 1
        
        return res
    
    
    
    def findCount_mine(self, nums, target):
        
        i= self.bin_search(nums, target)
        
        if i == -1:
            return 0
        
        l, r = self.expand(nums, i)
        
        return r - l
    
    
    def expand(self, nums, i):
        
        val= nums[i]
        
        l= i
        while l-1 >= 0 and nums[l-1] == val:
            l-=1
        
        r= i
        while r+1 < len(nums) and nums[r+1] == val:
            r+= 1
        
        r+= 1
        
        return (l, r)
    
    def bin_search(self, nums, target):
        
        lo, hi = 0, len(nums) -1
        
        while lo <= hi:
            
            mid_idx= (lo+hi)/2
            mid_val= nums[mid_idx]
            
            if mid_val == target:
                return mid_idx
            
            if target < mid_val:
                # look for target in the left half
                hi= mid_idx - 1
            
            else: # target > mid_val
                # look for target in the right half
                lo= mid_idx + 1
            
        return -1 # not found
