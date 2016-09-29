class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        
        if A==0: return []
        
        rows= [[0]*(i+1) for i in xrange(A)]
        
        rows[0]= [1] # the first row of pascal's triangle
        
        for i in xrange(1, A):
            
            rows[i][0]= 1
            
            # note row i of pascal's triangle has i+1 elements
            length= i+1
            for j in xrange(1, length - 1):
                rows[i][j]= rows[i-1][j-1] + rows[i-1][j]
                
            rows[i][length-1]= 1
    
        return rows

sol= Solution()
print sol.generate(5)