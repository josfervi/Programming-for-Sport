class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        
        if A == 0: return "0"
        
        str_acc= ""
        
        while A > 0:
            
            str_acc= str(A % 2) + str_acc
            A/= 2
            
        return str_acc
