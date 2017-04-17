class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        
        n= len(A)
        
        # the trick:
        
        # Let A[x,y] denote the value A[y][x]
        
        # the value A[       x,       y] goes to position (n-1)-y,       x
        # the value A[ (n-1)-y,       x] goes to position (n-1)-x, (n-1)-y
        # the value A[ (n-1)-x, (n-1)-y] goes to position       y, (n-1)-x
        # the value A[       y, (n-1)-x] goes to position       x,       y meaning A[x,y] should become A[y,l-x]
        
        l= n-1
                       # when                     when
                       # n is even                n is odd
        for x in xrange( n/2       if n%2==0 else n/2 +1   ):
            
            for y in xrange( n/2 ):
                
                A[y][x], A[x][l-y], A[l-y][l-x], A[l-x][y] = A[l-x][y], A[y][x], A[x][l-y], A[l-y][l-x]
        
        return A