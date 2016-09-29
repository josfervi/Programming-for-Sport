# which is easier to understand conceptually?

# (prev, curr)
#
# or
#
# (prev -> curr, curr -> next)

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        
        n= A
        
        if n == 1:
            return '1'
        
        i= 2
        prev= '1'  # holds the i-1th count-and-say number
        curr= '11' # holds the   ith count=and=say number
        
        # the current count-and-say number can be obtained from the previous count-and-say number
        while i <= n:
            
            curr= ""
            j= 0
            while j < len(prev):
                # j iterates through the digits of prev
                digit_ch= prev[j] # holds the jth digit of prev
                count= 0
                while j < len(prev) and prev[j] == digit_ch:
                    count+= 1
                    j+= 1
                
                curr+= str(count) + digit_ch
            
            # { prev holds i-1th count-and-say num }
            # { curr holds ith   count-and-say num }
            
            i+= 1
            
            # { prev holds i-1th count-and-say num }
            prev= curr
        
        # { i = n and curr = the nth count-and-say number }
        
        return curr
