class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        if A == []: return [1]
        
        i= len(A) - 1
        
        while i >= 0:
            if A[i] == 9:
                A[i]= 0
                i-= 1
            else:
                A[i]+= 1
                break
        
        # note: A of the original input and A after while loop are different
        
        # three cases
        # case | original input A                   | A, i after while loop
        #------+------------------------------------+----------------------
        #   1) |  i == -1                           |             i == -1
        #   1a)|    orig inp A is an empty list     |  A[0] dne,  i == -1
        #   1b)|    orig inp A is a list of 9's     |  A[0] == 0, i == -1
        #   2) |  original input A has leading 0's  |  A[0] == 0, i != -1
        #   3) |  neither case 2) nor 3)            |  A[0] != 0, i != -1
        
        # we have a choice in which order to check cases
        #  some orders are more readable
        #  some orders are more efficient - i.e. checking for the most likely case first,
        #                                        checking for the second most likely case second,
        #                                        etc.

        # checking in this order
        # PRO: does not require the initial check for empty A on line 6
        # 
        if i == -1:
            # case 1)
            # i == -1 signals overflow
            A.insert(0, 1)
            return A
        elif A[0] == 0:
            # case 2)
            return self.clean(A)
        # case 3)
        return A
        
        # checking in this order
        # CON: requires the initial check for empty A on line 6
        # if A[0] != 0:
        #     # case 3)
        #     return A
        # elif i == -1:
        #     # case 1)
        #     A.insert(0, 1)
        #     return A
        # # case 2)
        # return self.clean(A)
    
    # strip list A of any leading 0's
    # if A only contains 0's returns an empty list
    def clean(self, A):
        i= 0
        while A[i] == 0:
            i+= 1
        
        # A[i:] has no leading zeros
        return A[i:]
        
sol= Solution()
print sol.plusOne([9, 9, 9]) == [1, 0, 0, 0]
print sol.plusOne([0, 9, 9]) == [1, 0, 0]
print sol.plusOne([]) == [1]
print sol.plusOne([0])== [1]
print sol.plusOne([1, 2, 3]) == [1, 2, 4]
print sol.plusOne([9, 1, 9, 9]) == [9, 2, 0, 0]