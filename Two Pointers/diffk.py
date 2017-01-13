# https://www.interviewbit.com/problems/diffk/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    def diffPossible(self, A, B):
        if len(A) == 0:
            return 0
        i= 0
        j= 1                               # { i<j }
        while i < len(A)-1 and j < len(A): # { i<j } => { i<=j-1 } => { i is at most j-1 }
            if A[j] - A[i] == B:
                return 1
            elif A[j] - A[i] < B:
                j+= 1
            else:
                i+= 1
                j=  max(j, i+1)
                # if not i<j:
                #     assert i==j
                #     j= i+1
        
        return 0
    
    def my_diffPossible(self, A, k):
        
        # A is sorted
        # find i!=j, s.t. A[j] - A[i] = k
        # since k is non-negative, j>i
        
        if len(A) < 2:      return 0
         # --maxdiff-
        if A[-1]-A[0] <  k: return 0
        if A[-1]-A[0] == k: return 1
        
        if k == 0:
            # start return self.has_duplicate(A)
            prev_a= A[0]
            for curr_a in A[1:]:
                if prev_a == curr_a:
                    return 1
                prev_a= curr_a
            return 0
            # end   return self.has_duplicate(A)

        
        # start self.remove_duplicates(A)
        A= A[:] # A now points to a copy of input list A
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
        # end   self.remove_duplicates(A)

        min_i= 0 # i, if it exists, is ge min_i
        min_j= 1 # j, if it exists, is ge min_j
        
        while min_i < len(A)-1 and min_j < len(A):
            
            min_Ai= A[min_i]   # A[i], if it exists, is ge min_Ai
            
            min_Aj= min_Ai + k # A[j], if it exists, is ge min_Ai+k, since A[j] >= min_Ai + k
            target= min_Aj
            min_j_offset= self.binary_search(A[min_j:], target)
            min_j+= min_j_offset
            
            if min_j == len(A):
                return 0
            
            if A[min_j] == target:
                i= min_i # optional
                j= min_j # optional
                return 1
            min_Aj= A[min_j]
            
            min_Ai= min_Aj - k # A[i], if it exists, is ge min_Aj-k, since A[i] >= min_Aj - k
            target= min_Ai
            min_i_offset= self.binary_search(A[min_i:], target)
            min_i+= min_i_offset
            
            # if min_i == len(A): # this condition is
            #     return 0        # never trigered
            
            if A[min_i] == target:
                i= min_i # optional
                j= min_j # optional
                return 1
            
            min_Ai= A[min_i] # optional
        
        return 0
    
    # returns idx s.t. idx is the smallest index of lst s.t. target <= lst[idx]
    # note that this means that lst[idx-1] < target (if idx>0)
    def binary_search(self, lst, target):
        A, B = lst, target
    # start from # # https://www.interviewbit.com/problems/sorted-insert-position/
    # def searchInsert(self A, B):
        if B is []:   return 0
        if B < A[0]:  return 0
        if B > A[-1]: return len(A)
        
        l= 0
        r= len(A) -1
        
        mid= (l+r)/2
        # INVARIANT:
        # A[:l]   < B
        # A[r+1:] > B
        while l<=r:
            current= A[mid]
            if B < current:
                r= mid-1
            elif B == current:
                return mid
            else: # B > current
                l= mid+1
            mid= (l+r)/2
        assert l == r + 1
        # A[:l] < B
        # A[r+1:] = A[l:] > B
        #
        #         l 
        #         |
        #  _______v________
        # [  <B  |   >B    ]
        #  ----------------
        return l
    # end   from # # https://www.interviewbit.com/problems/sorted-insert-position/