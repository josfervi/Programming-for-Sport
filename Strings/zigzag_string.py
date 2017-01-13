# https://www.interviewbit.com/problems/zigzag-string/

# O( n ) time where n is the length of string
# O( 1 ) extra space

class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, string, num_rows):
        
        # espcial care to num_rows == 1
        # since r = 0 meets both special conditions:
        #  r == 0
        #  r == num_rows - 1
        if num_rows == 1:
            return string
        
        res= ""
                
        for r in xrange(0, num_rows):
            
            zigzag_idx= r
            in_step1=   True
            step1_inc=  2*num_rows-2-2*r
            step2_inc=  2*r
            
            while zigzag_idx < len(string):
                res+= string[zigzag_idx]
                
                if r == 0:
                    # always skip step2, since step2_inc = 2*r = 0
                    in_step1= True
                elif r == num_rows-1:
                    # always skip step1, since step1_inc = 2*num_rows-2-2*i = 0
                    in_step1= False
                
                if in_step1:
                    zigzag_idx+= step1_inc
                else:
                    zigzag_idx+= step2_inc
                
                # toggle in_step1
                in_step1 = not in_step1
        
        return res

# sol= Solution()
# print sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
# print sol.convert("ABCD", 2) == "ACBD"
# print sol.convert("B", 1) == "B" # requires special handling