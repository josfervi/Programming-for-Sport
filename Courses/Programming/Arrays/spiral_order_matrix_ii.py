# A_matrix[B][R : L -1: -1]= range(a, a +(R-L) +1)
    # error when L = 0 because
    # it interprets L-1=-1 as 
    # the last element, so
    # A_matrix[B][R:-1:-1]
    # is interpreted as an
    # empty list

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        
        L= 0    # indicates the leftmost  unpopulated col
        R= A -1 # indicates the rightmost unpopulated col 
        T= 0    # indicates the topmost   unpopulated row
        B= A -1 # indicates the bottomost unpopulated row
        
        d= 0 # direction
              # 0 - right
              # 1 - down
              # 2 - left
              # 3 - up
         
        A_matrix= [ [0]*A for i in xrange(A) ]
        
        a= 1 # the next unused value that goes into the next cell 
        while a <= A**2: # guaranteed to be finished exactly when a= A**2 +1
            
            if   d == 0:
                # populate right along the topmost unpopulated row
                A_matrix[T][L : R +1]= range(a, a +(R-L) +1)
                a+= (R-L) +1
                T+= 1
            
            elif d == 1:
                # populate down along the rightmost unpopulated col
                for y,a in zip( xrange(T, B +1), xrange(a, a +(B-T) +1) ):
                    A_matrix[y][R]= a
                a+= 1
                R-= 1
            
            elif d == 2:
                # populate left along the bottommost unpopulated row
                         #  going l to r
                # A_matrix[B][R : L -1: -1]= range(a, a +(R-L) +1) # error when L = 0 because
                                                                   # it interprets L-1=-1 as 
                                                                   # the last element, so
                                                                   # A_matrix[B][R:-1:-1]
                                                                   # is interpreted as an
                                                                   # empty list
                # two workarounds:
                # A_matrix[B][R : None if L -1==-1 else L -1 : -1]= range(a, a +(R-L) + 1)
                A_matrix[B][L : R +1]= range(a +(R-L), a -1, -1)
                a+= (R-L) +1
                B-= 1
            
            else:
                # d = 3
                # populate up along the leftmost unpopulated col
                for y,a in zip( xrange(B, T -1, -1), xrange(a, a +(B-T) +1) ):
                    A_matrix[y][L]= a
                a+= 1
                L+= 1
            
            # change to next direction
            d= (d+1) % 4 # d cycles through 0,1,2,3 and then wraps back around to 0
        
        return A_matrix