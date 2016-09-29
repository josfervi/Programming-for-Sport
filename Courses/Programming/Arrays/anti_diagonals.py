class Solution:
# @param a: list of list of integers
	# @return a list of list of integers
    def diagonal(self, a):
        
        R= len(a)    # num of rows
        C= len(a[0]) # num of cols
        
        # preprocess
        
        # lns 16 - 26 are not necessary.
        # they are necessary
        # if the problem were not for a square matrix,
        # but you still wanted your solution's output
        # to match the expected output given by
        # "See expected output"
        if C != R:
            if R > C:
                # extend the 2D array to have R cols
                for i in xrange(R):
                    a[i]+= [0]*(R-C)
            else:
                # {R < C}
                for i in xrange(R):
                    # truncate the 2D array to have R cols
                    a[i]= a[:R]
            C= R
        
        # {C= R}    
        # the result will be a list of length 2*C -1 
        
        len_= 2*C -1
        # antidiagonals= [ [0]*(d + 1   ) for d in xrange(C)       ]
        # antidiagonals+= [ [0]*(len_ - d) for d in xrange(C, len_) ]
        antidiagonals= [ [] for i in xrange(len_) ]
        
        # note:
        # for d in [0, C),
        #  the dth antidiagonal has length d+1
        #  the dth antidiagonal will be [ a[+0][d -0], a[+1][d -1], a[+2][d -2], ..., a[+d][d -d] ]
        #            # -len_-
        # for d in [C, 2*C -1),          # len_                                       
        #  the dth antidiagonal has length 2C-1 -d                              # ---(R-1)----  (d-(R-1))
        #  the dth antidiagonal will be [ a[d-C +1][C -1], a[d-C +2][C -2], ... a[d-C -d+C+R-1][C +d-C-R+1] ]
        
        # to see the above note, that for each a[j][i] in the dth diagonal i+j must equal d
        
        # traverse the 2D array from top to bottom, left to right, and
        # you'll come upon the elements of each antidiagonal in the correct order
        
        for j in xrange(R):
            for i in xrange(C):
                d= i+j
                antidiagonals[d].append(a[j][i]) # not the most efficient list operation
        
        return antidiagonals