# my solution was like 35 lines of code,
# I modified the given solution to be 22 lines of code

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        
        numsA= [int(a) for a in A.split('.')]
        numsB= [int(b) for b in B.split('.')]
        
        lenA= len(numsA)
        lenB= len(numsB)
        min_len= min( lenA, lenB )
        
        for i in xrange(min_len):
            if   numsA[i] > numsB[i]: return  1
            elif numsA[i] < numsB[i]: return -1
        
        # { numsA[:min_len] = numsB[:min_len]
        
        if   lenA > lenB:
            if sum(numsA[lenB:]) > 0: return  1
        elif lenA < lenB:
            if sum(numsB[lenA:]) > 0: return -1
        return 0
    
    
    def my_compareVersion(self, A, B):
        
        numsA= [int(a) for a in A.split('.')]
        numsB= [int(b) for b in B.split('.')]
        
        min_len= min( len(numsA), len(numsB) )
        
        i= 0
        while i<min_len and numsA[i] == numsB[i]:
            i+= 1
        
        if i == min_len:
            if   len(numsA) == len(numsB):
                return 0
            elif len(numsA) >  len(numsB):
                if numsA[i] != 0:
                    return 1
                else:
                    while i<len(numsA) and numsA[i] == 0:
                        i+= 1
                    if i == len(numsA):
                        return 0
                    else:
                        return 1
            else:
                if numsB[i] != 0:
                    return -1
                else:
                    while i<len(numsB) and numsB[i] == 0:
                        i+= 1
                    if i == len(numsB):
                        return 0
                    else:
                        return -1
        
        diff= numsA[i] - numsB[i]
        return diff / abs(diff)