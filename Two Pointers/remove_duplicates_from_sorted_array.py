# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    
    # much more efficient: doesn't do: A[i +1:]= A[j:]
    def removeDuplicates(self, A):
        
        idx=   0
        len_A= 0 # the number of unique elements encountered
        while idx<len(A):
            
            unique= A[idx]
            
            A[len_A]= unique
            len_A+=   1
            
            look_ahead= 1
            while idx+look_ahead<len(A) and A[idx+look_ahead] == unique:
                look_ahead+= 1
            
            if idx+look_ahead==len(A): break
            
            # { A[idx+look_ahead] != unique }
            idx+= look_ahead
        
        A[:]= A[:len_A] # modify A
        return len_A
    
    # much more efficient: doesn't do: A[i +1:]= A[j:]
    def removeDuplicates_2(self, A):
        
        i= 0
        j= 0
        len_A= len(A)
        while i<len(A):
            
            A[j]= A[i]
            j+= 1
            i+= 1
            
            if i<len(A) and A[i-1] == A[i]:
                
                # skip over all duplicates
                i+= 1
                len_A-= 1
                while i<len(A) and A[i-1] == A[i]:
                    i+= 1
                    len_A-= 1
        
        A[:]= A[:len_A] # modify A
        return len_A
    
    # - O(n) time complexity, where n = len(A) if we ignore the true cost of A[i +1:]= A[j:]
    # - O(1) extra space
    # - in place
    def removeDuplicates_1(self, A):
        
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

# sol= Solution()
# a= [ 0, 0, 0, 1, 1, 2, 2, 3 ]
# print a
# len_A= sol.removeDuplicates(a)
# print a