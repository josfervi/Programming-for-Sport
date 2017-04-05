def quotient(dividend, divisor):
    
    if divisor == 0:
        return None
    
    if dividend < 0 and divisor < 0:
        return quotient(-dividend, -divisor)
    
    if dividend < 0 and divisor >= 0:
        return -quotient(-dividend, divisor)
    
    if dividend >= 0 and divisor < 0:
        return -quotient(dividend, -divisor)
    
    
    mult_of_dsor = 0
    quot = 0
    
    while mult_of_dsor + divisor <= dividend:
        
        mm = divisor
        qq = 1
        
        while mult_of_dsor + mm + mm <= dividend:
            
            mm += mm
            qq += qq
        
        mult_of_dsor += mm
        quot += qq
    
    return quot


def test_quotient(a, b):
    
    num_tests_failed = 0
    
    for i in range(a, b):
        for j in range(a, b):
            if not test_passed(i, j):
                num_tests_failed += 1
                print "Failed test for {}, {}.".format(i, j)
    
    if num_tests_failed == 0:
        print "Passed all tests."
    else:
        print "Failed {} tests.".format(num_tests_failed)


def python_quotient_fixed(i, j):
    ''' Python's '/' (int division) operator
            does not do what you might
            expect for negative values
            of i, j. This fcn is the 'fixed'
            version s.t. i/j == (-i)/(-j) == -(-i)/j == -(i)/(-j)
    '''
    
    return int( float(i)/float(j) )

    
def test_passed(i, j):
    if j == 0:
        return quotient(i, j) == None
    return quotient(i, j) == python_quotient_fixed(i, j)


test_quotient(-100, 100)