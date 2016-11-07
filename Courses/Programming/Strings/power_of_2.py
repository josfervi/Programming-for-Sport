class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        
        # preprocess
        # remove leading zeros
        i= 0
        while i<len(A) and A[i] == '0':
            i+= 1
        # { A[:i] = 0 and A[i] != 0 }
        A= A[i:]
        
        if A == '' or A == '1':
            return 0
        
        # { A is a string of digits }
        A= [int(a) for a in A]
        # { A is a list of ints, each in [0...9] }
        carry_flag= False
        while A[-1] % 2 == 0:
            
            for i in xrange(len(A)):
                a= A[i]
                A[i]= a/2 + (5 if carry_flag else 0) # using the carry_flag set during the previous iteration
                carry_flag= a % 2 == 1 # a is odd
        
        # postprocess
        # remove leading zeros
        i= 0
        while i<len(A) and A[i] == 0:
            i+= 1
        # { A[:i] = 0 and A[i] != 0 }
        A= A[i:]
        
        if A == [1]:
            return 1
        return 0