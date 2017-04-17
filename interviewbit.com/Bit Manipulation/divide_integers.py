# https://www.interviewbit.com/problems/divide-integers/

class Solution:
    # @param dividend : integer
    # @param divisor : integer
    # @return an integer
    
    # O( log(n) ) where n is the number of bits
    def divide(self, dividend, divisor):
        
        m= dividend
        n= divisor
        
        sign= -1 if (m<0)^(n<0) else \
              +1
        
        m, n = abs(m), abs(n)
        
        q= 0           # n-1 where n is the bitlength of dividend, divisor
        for i in xrange(  31, -1, -1):
            if n << i <= m:
                m-= n << i
                q|= 1 << i # q+= 1 << i
        
        # q= sign*q
        # q= -q if sign == -1 else  q
        # q= -q if sign <   0 else  q
        q=  q if sign >   0 else -q
        
        return q if -2**31 <= q < 2**31 else 2**31 -1
        
    # O( result )
    def my_divide(self, dividend, divisor):
        
        divid= abs(dividend)
        divis= abs(divisor)
        sign= +1 if (dividend >= 0 and divisor > 0) or (dividend < 0 and divisor < 0) else \
              -1
        
        if divis == 0: raise  ZeroDivisionError("divisor must be non-zero")
        if divis == 1: return self.handle_overflow( sign* divid)
        if divis == 2: return self.handle_overflow( sign*(divid >> 1))
        
        quotient= 0
        while divid >= divis:
            divid-= divis
            quotient+= 1
        return self.handle_overflow(sign*quotient)
    
    def handle_overflow(self, res):
        if   res < -(2**31): return -(2**31)
        elif res > 2**31 -1: return   2**31 -1
        else:                return   res