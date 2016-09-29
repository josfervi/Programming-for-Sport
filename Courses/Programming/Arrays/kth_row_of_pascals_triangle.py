class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        
        if A==0: return [1]
        
        prev_row= [1]    + [0]*(A  )
        row=      [0]*(A+1)
        
        for i in xrange(1, A+1):
            
            row[0]= 1
            
            # note row i of pascal's triangle has i+1 elements
            length= i+1
            for j in xrange(1, length - 1):
                row[j]= prev_row[j-1] + prev_row[j]
                
            row[length-1]= 1
            
            prev_row= row[:]
    
        return row

sol= Solution()
print sol.getRow(5)
