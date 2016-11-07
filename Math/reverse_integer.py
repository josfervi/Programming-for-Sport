class Solution:
    # @param A : integer
    # @return an integer
    
    def reverse(self, A):
        
        A= str(A)
        
        if A[0] == '-': # equivalent to A < 0
            A= '-' + A[1:][::-1]
        else:
            A=       A[::-1]
            
        result= int(A)
        
        # check if the result overflows
        
        min_int_value= -2**31
        max_int_value=  2**31 -1
        
        if result < min_int_value or result > max_int_value:
            return 0
        
        return result
    
    def reverse2(self, A):
        
        acc= ""
        
        if A < 0:
            acc+= "-"
            A*= -1
        
        # chance for optimization:
        #  return 0 if len( list(reversed(str(A))) ) > 10 because that means that the result will overflow
        for a in reversed(str(A)):
            acc+= a
            
        # the for loop basically does acc= str(A)[::-1]
        
        result= int(acc)
        
        # check if the result overflows
        
        min_int_value= -2**31
        max_int_value=  2**31 -1
        
        if result < min_int_value or result > max_int_value:
            return 0
        
        return result
