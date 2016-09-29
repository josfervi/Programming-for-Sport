class Solution:
    
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        if len(X) != len(Y):
            return "error"
        
        if len(X) <= 1:
            return 0
        
        prev_x= X[0]
        prev_y= Y[0]
        acc= 0
        for x,y in zip(X[1:],Y[1:]):
            
            dx= abs(x - prev_x)
            dy= abs(y - prev_y)
            
            # let prev_P= (prev_x, prev_y)
            # let      P= (     x,      y)
            # diagonal= min(dx,dy)            is the num of diagnoal steps that must be taken in the min path bt P and prev_P
            # straight= max(dx,dy) - diagonal is the num of straight steps that must be taken in the min path bt P and prev_P
            # min_steps= diagonal + straight = max(dx,dy)

                  # min num of steps bt P and P_prev
            acc+= max( dx, dy )
            prev_x= x
            prev_y= y
        
        return acc
        
sol= Solution()
X= [ 1, 4, 6, 3, 7, 4, 2, 7, 8 ]
Y= [ 2, 5, 2, 1, 6, 8, 9, 2, 6 ]
print sol.coverPoints(X,Y) == 30