# https://www.interviewbit.com/problems/sort-by-color/

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        # use bucket sort
        
        r_cnt= 0 # red   is repr by 0
        w_cnt= 0 # white is repr by 1
        b_cnt= 0 # blue  is repr by 2
        
        S= 0
        
        for a in A:
            b_cnt+= (a==2)
            S+= a
        
        w_cnt= S - (b_cnt << 1)
        r_cnt= len(A) - w_cnt - b_cnt
        
        A[:]= [0]*r_cnt + [1]*w_cnt + [2]*b_cnt # modify A
        
        return A