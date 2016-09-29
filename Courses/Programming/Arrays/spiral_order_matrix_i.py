class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        num_rows= len(A)
        num_cols= len(A[0])
        
        A_t= zip(*A) # transpose of A
        
        # Let C be the submatrix of A with
        #  top    boundary, T
        #  bottom boundary, B
        #  left   boundary, L
        #  right  boundary, R
        T= 0
        B= num_rows-1
        L= 0
        R= num_cols-1
        dir= 0
        
        while T<=B and L<=R:
            
            if dir==0:
                # traverse across the topmost row of C from left to right
                result+= ( A[T][L:R+1] )
                T+= 1

            elif dir==1:
                # traverse across the rightmost col of C from top to bottom
                result+= ( A_t[R][T:B+1] )
                R-= 1
            
            elif dir==2:
                # traverse across the bottommost row of C from right to left
                result+= ( A[B][R: (None if L==0 else L-1) :-1] )
                B-= 1
                
            else: # {dir==3}
                # traverse across the leftmost col of C from bottom to top
                result+= ( A_t[L][B:(None if T==0 else T-1):-1] )
                L+= 1
            
            dir= (dir+1) % 4
            
        return result