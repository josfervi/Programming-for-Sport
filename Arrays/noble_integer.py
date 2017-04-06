# https://www.interviewbit.com/problems/noble-integer/

# gt := greater than
# ge := greater than or equal to

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, nums):
        
        nums.sort()
        nums.reverse()
        
        # nums are in descending order
        #  there are 0 numbers ge nums[0]
        #  there is  1 number  ge nums[1], the number  at nums[0]
        #  there are 2 numbers ge nums[2], the numbers at nums[:2]
        #  there are 3 numbers ge nums[3], the numbers at nums[:3]
        #  etc...
        prev_num = None
        for i, num in enumerate(nums):
            if num == i:
                if num != prev_num:
                    # prev_num > num
                    # in fact
                    # nums[:i] > num
                    # meaning there are
                    # i = num numbers in nums gt num
                    return 1
            prev_num = num
        return -1

# gotcha:
# getting rid of duplicates before doing sort() and reverse() does not work
# 
# for example, given the following list
# 
# [ 1, 2, 7, 0, 9, 3, 6, 0, 6 ]
# 
# [ 1, 2, 7, 0, 9, 3, 6 ] # after removing duplicates
# 
# [ 0, 1, 2, 3, 6, 7, 9 ] # after sorting
# 
#   0  1  2  3  4  5  6
# [ 9, 7, 6, 3, 2, 1, 0 ] # after reversing
# 
# while it is true that there are 3 unique numbers
# (9, 7, 6) that are gt 3, there are actually
# 4 numbers that are gt 3 in the original list
# (9, 7, 6, 6)