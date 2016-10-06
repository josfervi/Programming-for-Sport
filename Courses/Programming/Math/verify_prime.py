class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        
        if A <= 1: return 0
        if A <= 3: return 1
        
        if A % 2 == 0: return 0
        if A % 3 == 0: return 0
        
        sqrt_= int(A**0.5)
        i= 5
        add2= True
        while i <= sqrt_:
            if A % i == 0: return 0
            
            if add2:
                i+= 2
                add2= False
            else:
                i+= 4
                add2= True
        
        return 1