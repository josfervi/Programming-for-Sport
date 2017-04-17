class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        
        if num & (num-1) != 0:
           return False
        
        return num & 0b0101010101010101 == num