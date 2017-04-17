# https://www.interviewbit.com/problems/matrix-median/

def bin_search(nums, target):
    
    lo, hi = 0, len(nums) - 1
    
    while lo <= hi:
        
        mid_idx= (lo+hi)/2
        mid_val= nums[mid_idx]
        
        if mid_val == target:
            l, r = expand(nums, mid_idx)
            times_found= r - l
            # {nums[l:r] == target}
            return (times_found, (l, r))
        
        if target < mid_val:
            hi= mid_idx - 1
        else: # target > mid_val
            lo= mid_idx + 1
    
    times_found= 0
    return (times_found, (lo, lo))

# PRECONDITION: 0 <= idx < len(nums)
def expand(nums, idx):
    
    n= len(nums)
    
    val= nums[idx]
    
    l= idx
    while l-1 >= 0 and nums[l-1] == val:
        l-= 1
    
    r= idx
    while r+1 < n and nums[r+1] == val:
        r+= 1
    
    r+= 1
    # {l is the smallest int and r is the biggest int s.t. nums[l:r] == val}
    
    return (l, r)


# N - number of rows
# M - number of cols
# R - range of the values in the matrix, i.e. max(matrix) - min(matrix)

# O( lgR * N * lgM ) time
# O(1)               working space

# in the worst case, max(matrix) == MAX_INT, min(matrix) == MIN_INT,
# s.t. R = MAX_INT - MIN_INT = 2**32,
# even in this ridiculous worst case, lgR == 32
# so no biggie!

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, matrix):
        
        num_rows= len(matrix)
        
        if num_rows == 0:
            return None
        
        num_cols= len(matrix[0])
        
        length= num_rows * num_cols
        
        target_idx= length/2 # the median's idx
        
        FIRST= 0
        min_= min(matrix, key= lambda row : row[FIRST])[FIRST]
        
        LAST= -1
        max_= max(matrix, key= lambda row : row[LAST])[LAST]
        
        # search for median in min_ ... max_
        
        c_min, c_max = min_, max_
        
        while c_min <= c_max:
            
            candidate= (c_min+c_max)/2
            
            times_found_overall= 0
            l_overall= 0
            r_overall= 0
            
            for row in matrix:
                
                (times_found, (l, r)) = bin_search(row, candidate)
                
                times_found_overall+= times_found
                l_overall+= l
                r_overall+= r
            
            # { overall_sorted[l_overall:r_overall] == candidate }
            
            if l_overall <= target_idx < r_overall:
                return candidate
            
            elif target_idx < l_overall:
                # discard candidates >= candidate
                c_max= candidate - 1
                
            else: # target_idx >= r_overall
                # discard candidates <= candidate
                c_min= candidate + 1
        
        # if you reach this point something went horribly wrong!!!
        print "HALTing AND CATCHing FIRE..." # cause you might as well, lol
        # thankfully it never came to this jaja
        return