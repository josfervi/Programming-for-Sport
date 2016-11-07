# checks for divisibility by i,
#            for i <= int(sqrt(A)),
#            where i is 2,3 or a number not divisible by 2 nor 3
# 
# e.g.
# checks for divisibility by 2
#            divisibility by 3
#            divisibility by numbers of the form 6k+/-1, k=1,2,3,...
#                            which have the special property that they are
#                            neither divisible by 2 or 3
#                            the first few are:
#                            5, 7, 11, 13, 17, 19, 23, 25, ...
#                            note that they contain all the primes >= 5
# up to the largest number of the form 6k+/-1 that is <= int(sqrt(A))

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