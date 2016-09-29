# i didn't feel like optimizing the factorial,
# (prev fact(l -1) be used to obtain fact(l -1 -1) in O(1)
# whereas computing fact(l -1 -1) from scratch is O(l) whatever l happens to be
# note that l decreases down to 0

# the loop can also be run in the other direction
#  l would grow from 0,1,2 to len(A) -1
#  sorted_A would start with A[-1] and would grow to have each a in A

from math import factorial

class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        
        l= len(A)
        
        if l <= 1:
            return 1
            
        m= 1000003
        
        sorted_A= sorted(A)
        
        rank= 0
        for i,ch in enumerate(A[:-1]):
            
            ch_rank= sorted_A.index(ch)
            rank+= ( ch_rank * factorial(l -1) ) % m
            rank%= m
            
            sorted_A.remove(ch)
            l-= 1
        
        return (rank +1) % m
        
# sol= Solution()
# print sol.findRank("DTNGJPURFHYEW")
# print sol.findRank("abcd")
# print sol.findRank("abdc")
# print sol.findRank("acbd")
# print sol.findRank("acdb")
# print sol.findRank("adbc")
# print sol.findRank("adcb")
# print sol.findRank("bacd")
# print sol.findRank("badc")
# print sol.findRank("bcad")
# print sol.findRank("bcda")
# print sol.findRank("bdac")
# print sol.findRank("bdca")
# print sol.findRank("cabd")
# print sol.findRank("cadb")
# print sol.findRank("cbad")
# print sol.findRank("cbda")
# print sol.findRank("cdab")
# print sol.findRank("cdba")
# print sol.findRank("dabc")
# print sol.findRank("dacd")
# print sol.findRank("dbac")
# print sol.findRank("dbca")
# print sol.findRank("dcab")
# print sol.findRank("dcba")
