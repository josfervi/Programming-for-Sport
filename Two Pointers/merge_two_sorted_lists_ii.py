# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    
    # - O(m+n) time complexity
    # - O(m+n) extra
    def merge(self, A, B):
        
        m, n = len(A), len(B)
        
        res= [None]*(m+n)
        
        i= j= k= 0
        while i<m and j<n:
            if   A[i] <  B[j]:
                res[k]= A[i]
                i+= 1
            elif A[i] == B[j]:
                res[k:k+2]= [A[i]]*2
                i+= 1
                j+= 1
                k+= 1
            else:
                res[k]= B[j]
                j+= 1
            k+= 1
        
        res[k:]= B[j:] if i == m else A[i:]
        
        # modify A so that it points to res
        # A= res does not work
        A[:]= res
        
        return A
    
    # - O(m+n) time complexity
    # - O(1)   extra space
    def my_merge(self, A, B):
        
        m= len(A)
        n= len(B)
        A+= [None]*n # make space in list A for list B
        
        i, j = 0, 0
        len_A= m
        # INVARIANT:
        # { A[       : len_A ] == merge(A[:i], B[:j]) } 
        # { A[ len_A :       ] == [None]*(m+n-len_A)  }
        while i < len_A and j < n:
            if A[i] <= B[j]: i+= 1
            else:
                len_block_B= 1
                while j + len_block_B < n and B[j + len_block_B] <= A[i]:
                    len_block_B+= 1
                
                # Let block_B = B[ j : j + len_block_B ]
                # { A[:i] <= block_B <= A[i] <= A[i:len_A]
                #   meaning each element in A[:i]    is le each element in block_B and 
                #           each element in block_B} is le                 A[i]    and
                #                           A[i]     is le each element in A[i:len_A] }
                
                # desire: A= A[:i] + block_B + A[i:len_A] + [None]*(smthg)
                
                i_new=     i     + len_block_B
                j_new=     j     + len_block_B
                len_A_new= len_A + len_block_B
                
                A[i_new : len_A_new      ]= A[i : len_A          ]
                A[i     : i + len_block_B]= B[j : j + len_block_B]
                
                i=         i_new
                j=         j_new
                len_A= len_A_new
        
        if j != n:
            A[len_A:]= B[j:]
        
        return A