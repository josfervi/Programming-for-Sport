# uses Kadanes algorithm

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        
        # this solution is very similar to the MAX SUM CONTIGUOUS SUBARRAY soltuion
        
        if A[-1] == '\n':
            A= A[:-1] # ignore A[-1] because A[-1] = '\n'
        
        max_delta_ending_here= max_delta_so_far= -1 if A[0]=="1" else 1 # else case: A[0] = '0'
        L_h= R_h= 1
        L=   R=   1
        
        for i in xrange(1, len(A)):
            a= A[i]
            delta_a= -1 if a=="1" else 1
            
            if max_delta_ending_here+delta_a >= delta_a:
                # L_h is unchanged
                R_h+= 1
                max_delta_ending_here+= delta_a
            else:
                L_h= R_h= i +1
                max_delta_ending_here=  delta_a
                
            if max_delta_so_far >= max_delta_ending_here:
                # L, R, max_delta_so_far are unchanged
                pass
            else:
                L= L_h
                R= R_h
                max_delta_so_far= max_delta_ending_here
            
            # max_delta_ending_here= max(delta_a, max_delta_ending_here+delta_a)
            # max_delta_so_far=      max(max_delta_so_far, max_delta_ending_here)
        
        if max_delta_so_far == -1:
            return []

        return [L, R]
        
# sol= Solution()
# print sol.flip("1101")