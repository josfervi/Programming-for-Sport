class NumStr(str):
    
    # self :: decimal representation
    #         of num, a positive integer
    def toBinary(self):
        ''' Returns bits, a list of 0's and 1's,
            where bits[i] is the ith bit of the binary
            representation of num '''
        
        # I think we can convert to any base, b,
        # by replacing the 2 with b,
        # but I'd have to think about it a little bit more. 
        
        n = self
        
        bits = []
        
        while not (n == '' or n == '0'):
            n_divBy_2, n_modBy_2 = n.divModBy(2) # n/2 as a NumStr, n%2 as an int
            bit = n_modBy_2
            bits.append(bit)
            
            n = n_divBy_2
            
        return bits
    
    # self :: decimal representation
    #         of num, a positive integer
    def modBy2(self):
        ''' Returns num % 2 as an int '''
        
        lsd = int( self[-1] ) # least significant digit
                              # of the decimal represenation of num
        return lsd % 2
    
    # self :: decimal representation
    #         of num, a positive integer
    def divModBy(self, divisor):
        ''' Returns (num / divisor, num % divisor) as (NumStr, int) tuple '''
        
        BASE = 10
        
        _div = [None] * len(self)
        
        c_out = 0 # carry_out
        
        for i, digit in enumerate(self):
            
            c_in = c_out # carry_in
            current_dividend = BASE*c_in + int(digit)
            
            _div[i] = str(current_dividend / divisor)
            c_out   =     current_dividend % divisor
        
        div = NumStr(''.join(_div))
        mod = c_out
        
              # num/divisor, num%divisor
        return (  div,         mod      )



# n :: decimal string representation
#      of a positive integer, num
#      of at most 309 digits
def answer(n):
    
    # num can be very large so leave it as
    # and process it as a string, a NumStr
    n = NumStr(n)
    
    # this is a binary-math problem at heart,
    # so change num's representation to binary
    bits = n.toBinary() # lists of 0's and 1's where bits[i] is the ith bit of num
    
    number_of_operations = 0
    
    FIRST, SECOND = 0, 1
    
    while bits != [1]:
        
        lsb  = bits[FIRST] # least-significant bit
        
        number_of_operations += 1
        
        if lsb == 0:
            # { bits.repr == 1...0 }
            #
            # perform divide by 2 operation
            
            bits = bits[1:] # this can conceivably be done in O(1) time by pointing the pointer to the bits[1] instead of bits[0]
                            # if it turns out it is not actually done in O(1), I could work with the reversed list or use a collections.deque
            
            # { bits.repr == 1... }
            continue
        
        # { lsb == 1 }
        
        slsb = bits[SECOND] # second-least-significant bit
        
        if slsb == 0:
            # { bits.repr == 1...01 }
            #
            # perform a minus 1 operation
            
            bits[FIRST] = 0
            
            # { bits.repr == 1...00 }
            #
            # note: in the next two iterations, you will do two divide by 2 operations
        
        else: # slsb == 1
            # { bits.repr == 1...11 }
            #
            # perform a plus 1 operation
            
            bits[FIRST]  = 0
            bits[SECOND] = 0
            bits[2:]     = add1(bits[2:])
            
            #                   1...00
            #    1...11             11         1...00
            #    +    1  ==          1  ==        100
            # ---------      ---------      ---------
            # bits.repr      bits.repr      bits.repr
            #
            # note: in the next two iterations, you will do two divide by 2 operations
    
    return number_of_operations


# in-place
def add1(bits):
    
    i = 0
    while i < len(bits) and bits[i] == 1:
        bits[i] = 0
        i+= 1
    
    if i == len(bits):
        bits.append(1)
        return bits
    
    # { bits[i] == 0 }
    
    bits[i] = 1
    return bits

# TESTING

if __name__ == "__main__":
    
    uptothisNum = 50
    for num in range(1, uptothisNum):
        
        n = str(num)
        
        print num, answer(n)