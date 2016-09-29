class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        # n+1 = len(A)
        n= len(A) - 1
        B= [-1]*n # will store i in B[i -1]
        for a in A:
            if   B[a -1] == -1:
                B[a -1]= a
            elif B[a -1] == a:
                return a
            else:
                "error"
        return -1