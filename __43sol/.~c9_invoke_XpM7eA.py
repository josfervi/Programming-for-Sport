from inspect import getframeinfo, stack


def get_caller():
    # The caller (the file with the implemantation)
    # calls this file's test(impl) function
    # and the test(impl) function calls this get_caller() fcn,
    # so the caller is twice removed at this point,
    # hence the caller is at pos 2 in the call stack.
    CALLER = 2
    FRAMEOBJ = 0
    caller_frameobj = stack()[CALLER][FRAMEOBJ]
    caller = getframeinfo(caller_frameobj)
    return caller


def test(impl):
    """
    Black box tests of decompress function.
    You must pass in the specific implementation (impl).
    R
    """
    
    caller = get_caller()
    print "Testing implementation found in the following file: {}.".format(caller.filename)
    print "Testing implementation found in the following file: {}.".format(caller.filename)
    
    compressed_str = '2[f3[2[a]z]c]0[b]10[d]'
    expected_result = 'faazaazaazcfaazaazaazcdddddddddd'
    assert impl(compressed_str) == expected_result
    
    compressed_str2 = '2[f2[2[a]z]c]0[b]4[d]10[]'
    expected_result2 = 'faazaazcfaazaazcdddd'
    assert impl(compressed_str2) == expected_result2
    
    
    compressed_str3 = '0[3[z]f]'
    expected_result3 = ''
    assert impl(compressed_str3) == expected_result3
    
    print "Passed all tests."