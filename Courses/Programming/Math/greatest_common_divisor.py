# gcd(a, b) = gcd(b, a mod b)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        
        if B > A:
            A, B = B, A
        
        # { A >= B }
        
        while B != 0:
            A, B = B, A % B
        
        return A
