class NumStr(str):
    
    # self :: decimal representation
    #         of num, a positive integer
    def divModBy(self, divisor):
        ''' Returns (num / divisor, num % divisor) as (NumStr, int) tuple '''
        
        BASE = 10 #
        
        _result = [None] * len(self)
        
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
    
    act_div, act_mod = actual_result = NumStr(str(dividend)).divModBy(divisor)
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