# https://www.interviewbit.com/problems/sort-by-color/

class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        i = 0
        j = n - 1
        k = n - 1
        while i < k:
            if A[i] == 0:
                i += 1
            elif A[i] == 1:
                if i < j:
                    A[i],A[j] = A[j],A[i]
                    j-=1
                else:
                    i+= 1
            else:
                A[i],A[k] = A[k],A[i]
                k -= 1
                if j > k:
                    j = k
        return A