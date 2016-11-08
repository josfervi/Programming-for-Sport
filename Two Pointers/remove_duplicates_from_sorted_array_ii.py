# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        i= 0
        while i < len(A) -1: # { A[i-1] != A[i] for i>0 }
            
            if A[i] == A[i+1]:
                
                # erase all occurrences of A[i] in A[i+2:]
                j= i+2
                while j<len(A) and A[j] == A[i]: # { A[i+2:j] = A[i] }
                    j+= 1
                                                 # { A[j] != A[i] }
                A[i+2:]= A[j:]
                i= i+2
            
            else: i+= 1
        
        return len(A)