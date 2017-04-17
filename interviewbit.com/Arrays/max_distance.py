# the provided python code is O(n)

class Solution:
    
    def maximumGap(self, A):
        B= zip(range(len(A)), A)
        B= sorted(B, key= lambda b : b[1])
        
            # --ind--   # ---b---
        # A [ B[i][0] ] = B[i][1] for each i
        
        indeces= [ind for ind,b in B]
        # values=  [b   for ind,b in B]
        
        outp= self.max_(indeces) 
        
        max_so_far= -1
        for i in xrange(len(indeces)):
            max_so_far= max(max_so_far, outp[i] - indeces[i])
        
        return max_so_far
        
    def max_(self, inp):
        """Returns a list outp s.t. outp[i] is max( inp[i:] ) for each i"""
        outp= [-1]*len(inp)
        max_= -1000
        
        # max_ is max( inp[i:] )
        for i in xrange(len(inp) -1, -1, -1):
            max_= max(inp[i], max_)
            outp[i]= max_
        
        return outp


class mySolution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        
        if     A  == []: return -1
        if len(A) ==  1: return  0
        
        max_dist_so_far= -1
        i= 0
        j= len(A) -1
        while ( (i+max_dist_so_far +1) < len(A) ):
            if    (j-i) <= max_dist_so_far:
                a= A[i]
                i= self.find_next_smaller(A, a, i)
                if i == -1:
                    # there is no smaller next element
                    return max_dist_so_far
                j= len(A) -1
            elif A[i] <= A[j]:
                max_dist_so_far= j-i
                a= A[i]
                i= self.find_next_smaller(A, a, i)
                if i == -1:
                    # there is no smaller next element
                    return max_dist_so_far
                j= len(A) -1
            else:
                j-= 1
        
        return max_dist_so_far
                
    def find_next_smaller(self, A, a, i):
        """ Returns smallest ii s.t. ii > i and A[ii] < A[i] = a
            Returns -1 if no such ii exists, i.e. if A[ii] >= A[i] for all ii > i"""
        for ii in xrange(i+1, len(A)):
            if A[ii] < A[i]:
                return ii
        
        return -1
