from fractions import Fraction

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        if A == []: return ""
        
        # the cmp_ of ln32 can be algebraically converted into a key,
        # by noting that int(str(a) + str(b)) = a*10**len(b) + b...
        B= sorted(A, key= lambda a : Fraction(a, (10**len(str(a))) -1 ), reverse= True)
        
        B= self.clean_list(B)
        B= map(lambda b : str(b), B)
        return "".join(B)
        
    def clean_list(self, l):
        if l == []: return []
        
        i=0
        while l[i] == 0:
            i+= 1
            if i == len(l):
                # l is a list of 0s
                return [0]
        
        return l[i:]
    
    # works but not as efficient as largestNumber(self, A)
    def mySolution_largestNumber(self, A):
        
        if A == []: return ""
        
        cmp_= lambda a,b : int( str(a) + str(b) ) - int( str(b) + str(a) )
        
        B= sorted(A, cmp= cmp_, reverse= True)
        
        ## 1. accumulate elements of B into string acc
        ## 2. clean string acc of any leading "0"s
        ## 3, return
        # acc= ""
        # for b in B:
        #     acc+= str(b)
        # return self.clean_string(acc)
    
        ## this is probably faster
        ## because int comparison is prob faster than str comparison
        ## 1. clean int list B of any leading 0s
        ## 2. accumulate elements of B into string acc
        B= self.clean_list(B)
        # acc= ""
        # for b in B:
        #     acc+= str(b)
        # return acc
        
        # the following is equivalent
        B= map(lambda b : str(b), B) # map each int in B to the corresponding str
        return "".join(B)            # join all strings in B
    
    def clean_string(self, s):
        
        if s == "": return ""
        
        i= 0
        while s[i] == "0":
            i+= 1
            if i == len(s):
                # s is a string of "0"s
                return "0"
        
        return s[i:]