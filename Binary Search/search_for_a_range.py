# https://www.interviewbit.com/problems/search-for-a-range/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        
        l= 0
        r= len(A)
        # let b = A[s:t] s.t. for i     in range(s,t), A[i] == B and
        #                     for i not in range(s,t), A[i] != B
        
        # b is in A[l:r]
        
        mid= (l+r)/2
        while r > l:
            current= A[mid]
            if B < current:
                # B is in A[l:mid]
                # b is in A[l:mid]
                r= mid
            elif B == current:
                # s <= mid <= t
                # find s and t
                s= self.find_leftmost(A, B, l, mid)
                t= self.find_rightmost(A, B, mid, r)
                return [s, t]
            else: # B > current:
                # B is in A[mid+1:r]
                # b is in A[mid+1:r]
                l= mid+1
            mid= (l+r)/2
        
        return [-1, -1]
    
    def find_leftmost(self, lst, v, l, r):
        '''Given that lst is sorted and
                      lst[r] == v,
           Find the leftmost occurrence of v in lst[l:r +1]
        
        Result will be in range(l, r +1)
        PRECONDITION: for i < l, lst[i] != v'''
        
        if lst[l] == v: return l
        
        mid= (l+r)/2
        while r > l:
            current= lst[mid]
            if current < v:
                l= mid+1
            else: # current == v
                r= mid
            mid= (l+r)/2
        
        assert l == r
        return l
    
    def find_rightmost(self, lst, v, l, r):
        '''Given that lst is sorted and
                      lst[l] == v,
           Find the rightmost occurence of v in lst[l:r]
        
        Result will be in range(l, r)
        PRECONDITION: for i >= r, lst[i] != v'''
        
        if lst[r -1] == v: return r -1
        
        mid= (l+r)/2
        while r > l:
            current= lst[mid]
            if current == v:
                l= mid
            else: # current > v
                r= mid-1
            mid= (l+r+1)/2
        
        assert l == r
        return r