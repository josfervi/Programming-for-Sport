def add(a, b):
    
    ''' Add two non-negative
            numbers a, b
            without using
            arithmetic operators
    '''
    assert a >= 0 and b >= 0
    
    if a == 0:
        return b
    if b == 0:
        return a
    
    s = a^b
    c_out = a&b
    c_in = c_out << 1
    
    return add(s, c_in)


def test_add(a, b):
    
    for i in range(a, b):
        for j in range(a, b):
            if not test_passed(i, j):
                print "Test failed for {}, {}.".format(i,j)


def test_passed(i, j):
    return add(i,j) == i+j


print test_add(-2, 2)