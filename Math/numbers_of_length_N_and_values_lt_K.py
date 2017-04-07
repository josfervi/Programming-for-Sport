# https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/

import math

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, digits, l, upper):
        
        if l <= 0:
            raise ValueError()
        if upper < 0:
            raise ValueError()
        
        if not digits:
            return 0
        
        len_upper = int(math.log10(upper)) + 1
        
        if l > len_upper:
            return 0
        
        N = len(digits)
        if l < len_upper:
            
            if l == 1:
                return N
            
            count = N**l
            
            if digits[0] == 0:
                count -= N**(l-1)
            
            return count
        
        # l == len_upper
        
        count_soFar = 0
        first_call = True
        return self._solve(digits, l, str(upper), count_soFar, first_call)
    
    
    def _solve(self, digits, l, upper, count_soFar, first_call):
        """
        PRECONDITION:
          l == len_upper == int(math.log10(upper)) + 1
        """
        
        if l == 0:
            assert not upper
            return count_soFar
        
        if l == 1:
            return count_soFar + cnt_lt_target(digits, int(upper))
        
        upper_MSD, upper_rem = int(upper[0]), upper[1:]
        
        c = cnt_lt_target(digits, upper_MSD)
        if first_call and digits[0] == 0:
            assert upper_MSD != 0
            c -= 1
        
        N = len(digits)
        count_soFar += c * (N**(l-1))
        
        if not contains(digits, upper_MSD):
            return count_soFar
        
        first_call = False
        return self._solve(digits, l-1, upper_rem, count_soFar, first_call)


def cnt_lt_target(nums, target):
    """
    PRECONDITION:
      nums has no duplicates
      nums is sorted
    """
    return bin_search(nums, target)


def contains(nums, target):
    """
    PRECONDITION:
      nums is sorted
    """
    idx = bin_search(nums, target)
    return idx != len(nums) and nums[idx] == target


def bin_search(nums, target):
    """
    PRECONDITION:
      nums is sorted
    """
    
    l, r = 0, len(nums)-1
    
    while l <= r:
        
        mid_idx = (l+r)/2
        mid_val = nums[mid_idx]
        
        if mid_val < target:
            l = mid_idx + 1
        elif mid_val == target:
            return mid_idx
        else:
            r = mid_idx - 1
    
    return l


# def perms(n, r):
    
#     if r < 0 or n < r:
#         return 0
    
#     prod = 1
#     while r > 0:
#         prod *= n
#         n -= 1
#         r -= 1
    
#     return prod