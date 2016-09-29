from operator  import mul

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        
        if A < B:
            A, B = B, A
        
        # { A >= B}
        return self.nCr(A-1 + B-1, B-1)
    
    # credit to dheerosaur on StackExchange
    # http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
    def nCr(self, n, r):
        r = min(r, n-r)
        if r == 0: return 1
        numer = reduce(mul, xrange(n, n-r, -1))
        denom = reduce(mul, xrange(1, r+1))
        return numer/denom