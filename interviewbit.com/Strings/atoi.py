class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        
        i= 0
        
        # ignore leading whitspace
        while i < len(A) and A[i] == ' ':
            i+= 1
        
        sign= +1
        if A[i] == '-':
            sign= -1
            i+= 1
        elif A[i] == '+':
            #sign= +1
            i+= 1
        # else: do not advance i
        
        digits= "0123456789"
        abs_int_num= 0
        while i < len(A) and A[i] in digits:
            abs_int_num*= 10
            abs_int_num+= int(A[i])
            i+= 1
        
        if abs_int_num >= 2**31:
            return 2**31 -1 if sign == +1 else -2**31
        
        # if abs_int_num = 2**31 -1, 2**31 -1 gets returned on ln33
        
        return sign*abs_int_num