# https://www.interviewbit.com/problems/median-of-array/

def valid(num):
    return not num is None

def median(nums):
    
    n= len(nums)
    
    odd_lengthed= (n % 2 == 1)
    
    if odd_lengthed:
        return nums[n/2]
    
    return (nums[n/2 - 1] + nums[n/2]) / 2.0


# O(lg m) time
# O(1)    working space

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        
        m= len(A)
        n= len(B)
        
        if m == 0:
            return median(B)
        if n == 0:
            return median(A)
        
        if m < n:
            A, B = B, A
            m, n = n, m
        
        length= m+n
        
        if length == 0:
            return None
        
        odd_lengthed= ( length % 2 == 1 )
        
        target_idx= length / 2 # we are looking for the element at target_idx in the overall sorted lists, i.e. in merge_sort(A, B)
        
        lo, hi = 0, min( m, target_idx )
        
        while lo <= hi:
            
            i = (lo + hi) / 2
            j = target_idx - i
            
            # { 0 <= lo <= i <= hi <= min(m, target_idx) <= target_idx }
            
            # {i <= target_idx} implies {j>=0} i.e. {j cannot go negative}
            
            # { 0 <= lo <= i <= hi <= m } and { 0 <= j <= n }
            
            if j > n:
                # look for smaller j, bigger i by looking in the right half
                lo= i + 1
                continue
            
            A_i, A_im1, B_j, B_jm1 = self.get_values(A, B, i, j)
            
            if valid(A_im1) and valid(B_j) and A_im1 > B_j:
                # look for smaller A[i-1], bigger B[j] by looking for smaller i in the left half
                hi= i - 1
            
            elif valid(B_jm1) and valid(A_i) and B_jm1 > A_i:
                # look for smaller B[j-1], bigger A[i] by looking for bigger i in the right half
                lo= i + 1
            
            else:
                break
        
        element_at_target_idx=  self.min_( A_i, B_j )
        
        if odd_lengthed:
            return element_at_target_idx
        
        element_at_target_idxm1= self.max_( A_im1, B_jm1 )
        return ( element_at_target_idxm1 + element_at_target_idx ) / 2.0
    
    def min_(self, a, b):
        
        if valid(a) and valid(b):
            # {a is not None} and {b is not None}
            return min(a, b)
        
        # {exactly one of a,b is None}
        
        return a if valid(a) else b
    
    def max_(self, a, b):
        
        if valid(a) and valid(b):
            # {a is not None} and {b is not None}
            return max(a, b)
        
        # {exactly one of a,b is None}
        
        return a if valid(a) else b
        
    
    # PRECONDITIONS:
    #  1) 0 <= i <= len(A)
    #  2) - <= j <= len(B)
    def get_values(self, A, B, i, j):
        
        m, n = len(A), len(B)
        
        if i == 0:
            A_i=   A[0]
            A_im1= None
            must_break= True
        
        elif i == m:
            A_i=   None
            A_im1= A[m-1]
            must_break= True
        
        else:
            A_i=   A[i]
            A_im1= A[i-1]
        
        if j == 0:
            B_j=   B[0]
            B_jm1= None
            must_break= True
        
        elif j == n:
            B_j=   None
            B_jm1= B[n-1]
            must_break= True
        
        else:
            B_j=   B[j]
            B_jm1= B[j-1]
        
        return (A_i, A_im1, B_j, B_jm1)