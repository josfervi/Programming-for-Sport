    # def helper(self, ones, I, V, X ):
    #     if ones <= 3:
    #         return I*ones
    #     elif ones == 4:
    #         return I+V
    #     elif ones == 5:
    #         return V
    #     elif ones == 9:
    #         return I+X
    #     else:
    #         # { ones >= 6 and ones <= 8 }:
    #         return V + I*(ones - 5)

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman1(self, A):
        
        str_acc= ""
        
        thousands= A/1000
        str_acc+= 'M'*thousands
        
        A%= 1000
        
        hundreds= A/100
        
        if hundreds <= 3:
            str_acc+= 'C'*hundreds
        elif hundreds == 4:
            str_acc+= "CD"
        elif hundreds == 5:
            str_acc+= "D"
        elif hundreds >= 6 and hundreds <= 8:
            str_acc+= "D" + 'C'*(hundreds - 5)
        else:
            # { hundreds = 9 }
            str_acc+= "CM"
        
        A%= 100
        
        tens= A/10
        
        if tens <= 3:
            str_acc+= 'X'*tens
        elif tens == 4:
            str_acc+= "XL"
        elif tens == 5:
            str_acc+= "L"
        elif tens >= 6 and tens <= 8:
            str_acc+= "L" + 'X'*(tens - 5)
        else:
            # { tens = 9 }
            str_acc+= "XC"
        
        A%= 10
        
        ones= A/1
        
        if ones <= 3:
            str_acc+= 'I'*ones
        elif ones == 4:
            str_acc+= "IV"
        elif ones == 5:
            str_acc+= "V"
        elif ones >= 6 and ones <= 8:
            str_acc+= "V" + 'I'*(ones - 5)
        else:
            # { ones = 9 }
            str_acc+= "IX"
        
        return str_acc
    
    
    
    
    # using the helper
    def intToRoman(self, A):
        
        str_acc= ""
        
        thousands= A/1000
        str_acc+= 'M'*thousands
        A%= 1000
        
        hundreds= A/100
        str_acc+= self.helper(hundreds, 'C', 'D', 'M')
        A%= 100
        
        tens= A/10
        str_acc+= self.helper(tens, 'X', 'L', 'C')
        A%= 10
        
        ones= A/1
        str_acc+= self.helper(ones, 'I', 'V', 'X')
        
        return str_acc
        
    def helper(self, ones, I, V, X ):
        if ones <= 3:
            return I*ones
        elif ones == 4:
            return I+V
        elif ones == 5:
            return V
        elif ones == 9:
            return I+X
        else:
            # { ones >= 6 and ones <= 8 }:
            return V + I*(ones - 5)