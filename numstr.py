class NumStr(str):
    
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
            
        # remove leading zeros from _div, but if _div was all '0's don't remove the last '0', accomplished by i < len(_div)-1
        _div = removeLeadingZeros(_div)
        
        div = NumStr(''.join(_div))
        mod = c_out
        
              # num/divisor, num%divisor
        return (  div,         mod      )

# digits :: a list of strings or ints
def removeLeadingZeros(digits):
    
    i = 0
    while i < len(digits)-1 and int(digits[i]) == 0:
        i += 1
    
    # { digits[:i] == ['0']*i } <- the leading zeros
    
    return digits[i:]
    

def run_random_tests(number_of_tests):
    
    number_of_failed_tests = 0
    
    for i in range(number_of_tests):
        
        test_passed, failStr = test_divModBy_once()
        
        if not test_passed:
            number_of_failed_tests += 1
            print failStr
    
    if number_of_failed_tests == 0:
        print "Passed all {0} random test cases! :)".format(number_of_tests)
    else:
        print "Failed {0}/{1} random test cases. :(".format(number_of_tests, number_of_failed_tests)

from random import randint

# runs 
def test_divModBy_once():
    
    dividend = randint(0, 10**9)
    divisor  = randint(1, 2*dividend)
    
    expected_result = ( dividend / divisor, dividend % divisor )
    
    act_div, act_mod = actual_result = NumStr(dividend).divModBy(divisor) # no need to str(.) in NumStr(str(dividend))
    actual_result    = (int(act_div), act_mod)
    
    test_passed = expected_result == actual_result
    failStr     = None if test_passed else getFailStr(dividend, divisor, expected_result, actual_result)
    
    return (test_passed, failStr)

def getFailStr(dividend, divisor, expected_result, actual_result):
    
    exp_div, exp_mod = expected_result
    act_div, act_mod = actual_result
    
    failStr = \
    "Failed for {0}/{1}\n".format(dividend, divisor)      + \
    "\t     expected \t\t got\n"                          + \
    "\tDIV: {0}      \t\t {1}\n".format(exp_div, act_div) + \
    "\tMOD: {0}      \t\t {1}\n".format(exp_mod, act_mod)
    
    return failStr

if __name__ == "__main__":
    number_of_tests = 10**6
    run_random_tests(number_of_tests)
    
    print NumStr(1000).divModBy(100)  # w/o removing leading zeros,  prints ('0010', 0)
                                      # w/  removing leading zeros*, prints (  '10', 0)
    
    print NumStr(1000).divModBy(1001) # w/o removing leading zeros,  prints ('0000', 1000)
                                      # w/  removing leading zeros*, prints (   '0', 1000)
                                      
                                      # * := does not however remove the last element even if it would
                                      #      otherwise be considered part of the set of leading zeros
                                      #      because doing so would leave us with an empty string instea of '0'
    