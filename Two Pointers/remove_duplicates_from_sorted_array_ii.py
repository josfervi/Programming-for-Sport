# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    # @param A : list of integers
    # @return an integer
    
    # much more efficient: doesn't do: A[i+2:]= A[j:]
    def removeDuplicates(self, A):
        
        i= 0
        j= 0
        len_A= len(A)
        while i<len(A):
            
            A[j]= A[i]
            j+= 1
            i+= 1
            
            if i<len(A) and A[i-1] == A[i]:
                
                A[j]= A[i]
                j+= 1
                i+= 1
                
                # skip over all duplicates
                while i<len(A) and A[i-1] == A[i]:
                    i+= 1
                    len_A-= 1
        
        A[:]= A[:len_A]
        
        return len_A
    
    # does A[i+2:]= A[j:], which is not very efficient
    def removeDuplicates_1(self, A):
        
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