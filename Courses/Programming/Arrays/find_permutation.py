# the given solution, findPerm  loops only once! it's magical!
# my        solution, findPerm2

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        
        n= B
        acc=   [0]*n
        smallest_remaining_int= 1 # start
        largest_remaining_int=  n # upto
        
        # INVARIANT:
        # remaining ints = [start, upto] inclusive
        
        for i in xrange(n -1):
            if A[i] == 'D':
                # the next int must be less than the current int,
                # so let the current int be the largest remaining int
                acc[i]= largest_remaining_int
                largest_remaining_int-= 1
            else:
                # A[i] == 'I'
                # the next in must be greater than the current int,
                # so le the current int be the smallest remaining int
                acc[i]= smallest_remaining_int
                smallest_remaining_int+= 1
        
        # in each iteration of the for loop above,
        # the difference largest_remaining_int - smallest_remaining_int shrinks by 1
        # the initial difference is n-1
        # the loop runs for i= 0 to i= n -2, i.e. n-1 times
        # so the final difference is n-1 - (n-1) = 0
        
        # {smallest_remaining_int = largest_remaining_int}
        
        acc[n-1]= smallest_remaining_int
        
        return acc
    
    def findPerm2(self, A, B):
        
        n= B
        acc=    [0]*n
        acc[0]= 1
        min_so_far= 1
        max_so_far= 1
        
        for i,a in enumerate(A):
            if a == 'I':
                max_so_far= acc[i +1]= max_so_far +1 # replaces two lines of code
                                                     #  acc[i +1]=  max_so_far +1
                                                     #  max_so_far= max_so_far +1
            else:
                # {a = 'D'}
                min_so_far= acc[i +1]= min_so_far -1
        
        # in each iteration of the for loop above,
        #  the difference max_so_far - min_so_far increases by 1
        # the loop runs for n-1 iterations, therefore
        #  after the loop executes, max_so_far - min_so_far = n-1
        
        min_acc= min_so_far
        for i in xrange(len(acc)):
            acc[i]-= (min_acc -1)
            
        # each element in acc is in [1...n] inclusive as desired
        
        return acc