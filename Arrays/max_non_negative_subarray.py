class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        
        # a subarray consists of a left index, a right index, and a sum
        # e.g. the current subarray consists of L_c, R_c, and current_sum
        
        L=   R=   0       # A[L : R] >= 0
        max_sum_so_far= 0 #= sum(A[L : R])
        
        L_c= R_c= 0    # A[L_c : R_c] >= 0 meaning each element in A[L_c ; R_c] is >= 0
        current_sum= 0 #= sum( A[L_c : R_c] )
        
        i= 0
        while i < len(A):
            
            while i < len(A) and A[i] >= 0:
                # grow the current non-negative subarray
                R_c+= 1
                # assert R_c == i+1
                current_sum+= A[i]
                i+= 1
            
            # { i >= len(A) } or
            # { i <  len(A) and i=0 and                 A[i] < 0 } or
            # { i <  len(A) and i>0 and A[i-1] >= 0 and A[i] < 0 }
            
            if i != 0 and A[i-1] >= 0:
                
                # if the current subarray is 'greater' than max_so_far subarray,
                # set max_so_far subarray to current subarray
                
                (L, R, max_sum_so_far) = \
                    (L_c, R_c, current_sum) \
                if \
                    (current_sum >  max_sum_so_far) or \
                    (current_sum == max_sum_so_far and R_c-L_c >  R-L) or \
                    (current_sum == max_sum_so_far and R_c-L_c == R-L and L_c < L) \
                else \
                    (L, R, max_sum_so_far)
                
                # if current_sum > max_sum_so_far:
                #     L= L_c
                #     R= R_c
                #     max_sum_so_far= current_sum
                # elif current_sum == max_sum_so_far:
                #     if R_c-L_c > R-L:
                #         L= L_c
                #         R= R_c
                #         max_sum_so_far= current_sum
                #     elif R_c-L_c == R-L:
                #         if L_c < L:
                #             L= L_c
                #             R= R_c
                #             max_sum_so_far= current_sum
                
            while i < len(A) and A[i] <  0:
                # ignore the negative elements
                i+= 1
            
            # { i>= len(A) } or
            # { i<  len(A) and A[i-1] < 0 and A[i] >= 0 }
            
            if i >= len(A):
                break
            
            # { i<  len(A) and A[i-1] < 0 and A[i] >= 0 }
            
            # start a new non-negative subarray
            L_c= R_c= i
            current_sum= 0
        
        return A[L : R]