# https://www.interviewbit.com/problems/matrix-search/

'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem'''

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        
        if A    is []: return False
        if A[0] is []: return False
        row_index= self.identify_row(A, B)
        if row_index is None: return False
        return self.binary_search(A[row_index], B) is not None
    
    # complexity: O(num_rows)
    # can be made into O(log(num_rows))
    def identify_row(self, A, B):
        '''If integer B is in matrix A, returns the index of the row containing B. If multiple rows contain B, returns the smallest index.'''
        '''If integer B is not in matrix A and B<A[0][0] or B>A[-1][-1] returns None,
        otherwise, returns the index of the row where B would go.'''
        for i, row in enumerate(A):
             # 1st elem of row         last elem of row
            if row[0]          <= B <= row[-1]:
                return i
        return None
    
    def binary_search(self, lst, target):
        
        if lst is []:         return None
        if lst[0] == target:  return 0
        if lst[-1] == target: return len(lst) -1
        
        l= 0
        r= len(lst)
        # B is in lst[l:r]
        
        mid= (l+r)/2
        while l<r:
            current= lst[mid]
            if target < current:
                # target is in lst[l:mid]
                r= mid
            elif target == current:
                return mid
            else: # target > current
                # target is in lst[mid+1:r]
                l= mid+1
            mid= (l+r)/2
        return None