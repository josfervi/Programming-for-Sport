# my solution uses extra space,

# the provided solution does not use extra memory,
# the provided solution is developed by using
#  - the sum of the               elements of A
#  - the sum of [1, 2, 3, ... n]
#  - the sum of the square of the elements in A
#  - the sum of [1^2, 2^2, 3^2, ... n^2]
# it is a clever solution; however may lead to int overflow in some langs (not Python though)

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        dup= -1 # duplicate
        mis= -1 # missing
        
              # --n--
        B= [-1]*len(A) # will store number a in B[a -1]
                       # B[i] will store a = i+1
                       # 1 thru n wil be stored in B[0] thru B[n-1]
        for a in A:
            if   B[a -1] == -1:
                  B[a -1] = a
            elif B[a -1] == a:
                  dup= a
            else:
                "error"
        
        # B stores 1 thru n, except the missing number
        for i,b in enumerate(B):
            #            b = B[i] should store i+1 if i+1 is not missing from A
            # otherwise, b = B[i]        stores -1 if i+1 is     missing from A
            if b == -1:
                mis= i+1
                break
        
        return dup, mis