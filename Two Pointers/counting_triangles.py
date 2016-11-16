# https://www.interviewbit.com/problems/counting-triangles/

class Solution:
    # @param A : list of integers
    # @return an integer
    
    # space:   constant extra space
    # time:    quadratic time in len(A)
    # side fx: no side effects
    def nTriang(self, A):
        
        if len(A)<3: return 0
        
        A.sort() # sort A in-place
        
        res= 0
        
        for max_leg_idx in xrange(2, len(A)):
            
            min_leg_idx= 0
            mid_leg_idx= max_leg_idx-1
            
            max_leg_length= A[max_leg_idx]
            
            target= max_leg_length
            
            while True:
                if min_leg_idx >= mid_leg_idx: break
                
                min_leg_length, mid_leg_length = A[min_leg_idx], A[mid_leg_idx]
                
                if min_leg_length+mid_leg_length <= target: min_leg_idx+= 1
                else:
                    # { min_leg_length+mid_leg_length>max_leg_length }
                    res+= (mid_leg_idx - min_leg_idx)
                    mid_leg_idx-= 1
            
        return res % (10**9 + 7)