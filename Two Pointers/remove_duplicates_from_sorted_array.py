# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        i= 0
        
        # INVARIANT:
        # { unique(A[:i]) meaning each element in A[:i] is unique }
        while i < len(A) -1:
            if A[i] == A[i +1]:
                
                j= i +2
                
                # INVARIANT:
                # { A[i:j] = A[i] meaning each element in A[i:j] equals A[i] }
                while j < len(A) and A[i] == A[j]:
                    j+= 1
                # { A[i:j] = A[i] meaning each element in A[i:j] equals A[i] }
                # get rid of A[i +1:j] by overwritting A[i +1:] with A[j:]
                A[i +1:]= A[j:]
            i+= 1 # each increment of i signals a new unique element in A[:i]
        
        return len(A)