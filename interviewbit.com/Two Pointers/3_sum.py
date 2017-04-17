# https://www.interviewbit.com/problems/3-sum/

# avoid function calls in Python - they can mean the difference between passing and failing EFFICIENCY

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    # O( n**2 ) where n = len(A)
    def threeSumClosest(self, A, B): # using the hint
        
        A.sort() # O( nlogn )
        
        res= A[0] + A[1] + A[-1]
        
        for i in xrange(len(A) -2): # i < j < k <= len(A) -1
            
            j, k = i+1, len(A) -1
            
            targ_= B - A[i] # remaining
            res_= two_sum= A[j] + A[k]
            while not k-j == 1:
                if   two_sum <  targ_: j+= 1
                elif two_sum == targ_: return B
                else               : k-= 1
                two_sum= A[j] + A[k]
                # res_= self.closest(res_, two_sum, targ_) # solution is fails on EFFICIENCY if you call this function
                if abs(targ_ - two_sum) < abs(targ_ - res_):  # instead, straight up copy the fcn body here
                    res_= two_sum
            
            three_sum= A[i] + res_
            # res= self.closest(res, three_sum, B) # solution is fails on EFFICIENCY if you call this function
            if abs(B - three_sum) < abs(B - res):  # instead, straight up copy the fcn body here
                res= three_sum
        
        return res
    
    
    # I think O( n**2 ) but still fails on EFFICIENCY
    def my_threeSumClosest(self, A, B):
        
        A.sort() # O( nlogn )
        
        i, j, k = 0, 1, len(A) -1
        
        res= three_sum= A[i] + A[j] + A[k]
        
        while not (k-j == 1 and j-i == 1): # while i,j,k are not consecutive
            # two left
            #i, j, k = l, l+1, r
            while not k-j == 1:
                if   three_sum <  B: j+= 1
                elif three_sum == B: return B
                else               : k-= 1
                three_sum= A[i] + A[j] + A[k]
                # res= self.closest(res, three_sum, B)
                if abs(B - three_sum) < abs(B - res):
                    res= three_sum
            # j == k-1
            
            # two right
            #i, j, k = l, r-1, r
            while not j-i == 1:
                if   three_sum <  B: i+= 1
                elif three_sum == B: return B
                else               : j-= 1
                three_sum = A[i] + A[j] + A[k]
                # res= self.closest(res, three_sum, B)
                if abs(B - three_sum) < abs(B - res):
                    res= three_sum
            # i == j-1
        
        return res
    
    # I think O( n**2 ) but still fails on EFFICIENCY
    def my_optimized_threeSumClosest(self, A, B):
        
        A.sort() # O( nlogn )
        
        i, j, k = 0, 1, len(A) -1
        
        res= three_sum= A[i] + A[j] + A[k]
        
        while not (k-j == 1 and j-i == 1): # while i,j,k are not consecutive
            # two left
            #i, j, k = l, l+1, r
            targ_= B - A[i]
            res_= two_sum= A[j] + A[k]
            while not k-j == 1:
                if   two_sum <  targ_: j+= 1
                elif two_sum == targ_: return B
                else                 : k-= 1
                two_sum= A[j] + A[k]
                # res= self.closest(res, three_sum, B)
                if abs(targ_ - two_sum) < abs(targ_ - res_):
                    res_= two_sum
            three_sum= A[i] + res_
            if abs(B - three_sum) < abs(B - res):
                    res= three_sum
            # j == k-1
            
            # two right
            #i, j, k = l, r-1, r
            targ_= B - A[k]
            res_= two_sum= A[i] + A[j]
            while not j-i == 1:
                if   two_sum <  targ_: i+= 1
                elif two_sum == targ_: return B
                else                 : j-= 1
                two_sum = A[i] + A[j]
                # res= self.closest(res, three_sum, B)
                if abs(targ_ - two_sum) < abs(targ_ - res_):
                    res_= two_sum
            three_sum= res_ + A[k]
            if abs(B - three_sum) < abs(B - res):
                    res= three_sum
            # i == j-1
        
        return res
    
    def closest(self, a, b, target):
        if abs(target - a) < abs(target - b): return a
        else:                                 return b