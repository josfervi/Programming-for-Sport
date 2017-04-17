# https://www.interviewbit.com/problems/minimize-the-absolute-difference/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        i = j = k = 0
        
        a, b, c = A[i], B[j], C[k]
        M, m = max(a,b,c), min(a,b,c)
        best_soFar = M - m
        if a == m:
            i += 1
        if b == m:
            j += 1
        if c == m:
            k += 1
        
        while i < len(A) and j < len(B) and k < len(C):
            
            a, b, c = A[i], B[j], C[k]
            M, m = max(a,b,c), min(a,b,c)
            curr = M - m
            best_soFar = min(best_soFar, curr)
            if a == m:
                i += 1
            if b == m:
                j += 1
            if c == m:
                k += 1
        
        return best_soFar
