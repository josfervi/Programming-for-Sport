class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        
        L, M, N = len(A), len(B), len(C)
        i, j, k =     0,      0,      0
        
        min_max_diff= 2**31-1
        
        while i<L and j<M and k<N:
            
            a, b, c = A[i], B[j], C[k]
            # note; max(abs(a-b), abs(b-c), abs(c-a)) = max(a,b,c) - min(a,b,c)
            # hint: look at a,b,c on a number line
            max_= max(a,b,c)
            min_= min(a,b,c)
            potential_diff= max_ - min_
            min_max_diff= min( min_max_diff, potential_diff )
            
            if min_max_diff == 0: return 0
            
            if   a == min_: i+= 1
            elif b == min_: j+= 1
            else          : k+= 1
        
        return min_max_diff