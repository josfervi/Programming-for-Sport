# encoding

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        
        # seeing as this problem is under the encoding subheading,
        # and having thought about the problem for a while
        
        # I think the solution hinges on
        #  encoding two ints a,b each in [0...N-1] inclusive into
        #  one signed int that does not overflow
        # N*N does not overflow, so if we can encode any pair in [0...N-1]^2
        #  into an in <= N*N we're golden.
        
        # I will encode a,b into E s.t. E/N=b and E%N=a.
        #  Thus, E= b*N + a !yay!
        #  Note, thet E <= (N-1)*N + (N-1) = N^2 -N +N -1= N^2 -1. !yay!
        #   this guarantees that E does not overflow.
        
        # Let a=  original value   A[i],
        #     b=  original value A[A[i]]= original value A[a]
        # in step 1:
        #   each element A[i] in A becomes e= b*N + a. (encoding step)
        # even after A[i] has been changed by the encoding step, we can retrieve it's origina value
        #   by doing A[i] % N
        
        N= len(A)
        
        for i,a in enumerate(A):
            # a= original value A[i]
            
            # A[a] may have been 'encoded' itself, we must extract its original value
            b= A[a] % N # if A[a] was not 'encoded' this operation does nothing, so we're good
                # ---e---
            A[i]= b*N + a # A[i]+= b*N

        
        # in step 2:
        #   each element A[i]= e= b*N + a becomes b
        for i,e in enumerate(A):
            
            A[i]= e / N # e= a*N + b
        
        return A
        
        
