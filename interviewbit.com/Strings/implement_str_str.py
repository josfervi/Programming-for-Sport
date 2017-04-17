# needle in a haystack problem

class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        
        if needle == []:
            return -1
        
        for i in xrange( len(haystack) - len(needle) +1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1