class Solution:
    # @param A : string
    # @return a list of strings
    
    def restoreIpAddresses(self, A):
        n = len(A)
        if n < 4 or n > 12:
            return []
        ret = []
        i = 1
        while i <= 3 and i < n:
            j = i+1
            while j <= i + 3 and j < n:
                k = j + 1
                while k <= j + 3 and k < n:
                    #print A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:]
                    a = int(A[:i])
                    b = int(A[i:j])
                    c = int(A[j:k])
                    d = int(A[k:])
                    if (A[0] == '0' and i>1) or (A[i] == '0' and j>i+1) or (A[j] == '0' and k>j+1) or (A[k] == '0' and n>k+1):
                        pass
                    elif a <= 255 and b <= 255 and c <= 255 and d <= 255:
                        ret.append(A[:i]+'.'+A[i:j]+'.'+A[j:k]+'.'+A[k:])
                    k+= 1
                j+= 1
            i+= 1
        return ret
    
    
    
    # function calls really hurt python,
    # this version times out because of the function calls,
    # even though it's very similar to ther_restoreIpAddresses
    def our_restoreIpAddresses(self, A):
        n = len(A)
        if n < 4 or n > 12:
            return []
        ret = []
        i = 1
        while i <= 3 and i < n:
            a= A[:i]
            if not self.isValid(a): continue
            
            j = i+1
            while j <= i + 3 and j < n:
                b= A[i:j]
                if not self.isValid(b): continue
                
                k = j + 1
                while k <= j + 3 and k < n:
                    c= A[j:k]
                    d= A[k: ]
                    if not self.isValid(c) or not self.isValid(d): continue
                
                    #print A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:]
                    ret.append(A[:i]+'.'+A[i:j]+'.'+A[j:k]+'.'+A[k:])
                    k+= 1
                j+= 1
            i+= 1
        return ret
    # a is a string
    def isValid(self, a):
        if (a[0] == '0' and len(a) > 1):
            return False
        if int(a) > 255:
            return False
        return True
    
    
    
    def my_restoreIpAddresses(self, A):
        
        #if len(A) < 4 or len(A) > 12:
        #    return []
        
        #if len(A) == 4:
        #    return ['.'.join(A)]
        
        #if len(A) == 12:
        #    str_acc= ""
        #    for i in xrange(0, 12, 3):
        #        num_str= A[i : i+3]
        #        if int(num_str) > 255:
        #            return []
        #        str_acc= str_acc + num_str + '.'
        #    return [str_acc[:-1]]
        
        return self.helper(4, 0, "", A)
    
    # num is the number of ip sections left to determin, num is in [1...4]
    # s_i is the index where the current ip section must start
    # acc is a string containing the already constructed ip sections,
    #     there are 4 - num already constructed ip section(s)
    # A is the original string from which the valid ip addresses must be constructed
    def helper(self, num, s_i, acc, A):
        
        if len( A[s_i : ] ) < num or len( A[s_i : ]) > 3*num:
            return []
        
        if num == 1:
            if A[s_i] == '0' and len(A[s_i : ]) > 1:
                return []
            if len(A[s_i : ]) == 3 and int(A[s_i : s_i+3]) > 255:
                return []
            return [ acc + A[s_i : ] ]
        
        if A[s_i] == '0':
            return self.helper(num-1, s_i+1, acc + A[s_i : s_i+1] + '.', A)
        
        if int(A[s_i: s_i+3]) > 255:
            return self.helper(num-1, s_i+1, acc + A[s_i : s_i+1] + '.', A) +\
                   self.helper(num-1, s_i+2, acc + A[s_i : s_i+2] + '.', A)
        
        return self.helper(num-1, s_i+1, acc + A[s_i : s_i+1] + '.', A) + \
               self.helper(num-1, s_i+2, acc + A[s_i : s_i+2] + '.', A) + \
               self.helper(num-1, s_i+3, acc + A[s_i : s_i+3] + '.', A)