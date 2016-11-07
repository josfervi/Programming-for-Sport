class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        
        if len(A) < len(B):
            A, B = B, A
        
        # { len(A) >= len(B) }
        
        min_len= len(B)
        
        str_acc= ''
        carry_in= 0
        for i in xrange(-1, -min_len -1, -1):
            
            a= int(A[i])
            b= int(B[i])
    
            s= a ^ b ^ carry_in
            str_acc= str(s) + str_acc
            
            if a+b+carry_in >= 2:
                carry_in= 1
            else:
                carry_in= 0
        
        if carry_in == 0:
            return A[:-min_len] + str_acc
        
        # { carry_in = 1 }
        
        for i in xrange(-min_len -1, -len(A) -1, -1):
            
            a= int(A[i])
            
            s= a ^ carry_in
            str_acc= str(s) + str_acc
            
            carry_in= a and carry_in
        
        if carry_in == 1:
            return '1' + str_acc
        
        return str_acc

# sol= Solution()
# print sol.addBinary("11", "1")