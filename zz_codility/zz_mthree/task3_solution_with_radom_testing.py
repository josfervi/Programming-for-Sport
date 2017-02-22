def solution(N):
    return num_1s_in_ints_le(N) # the efficient solution
    # return num_1s_in_ints_le_brute_force(N)


# O(lg{{lgN}!}) time
# which is between O(lg{N}) and O(N) time
# according to WolframAlpha:
# https://www.wolframalpha.com/input/?i=limit+as+x+goes+to+infinity+(log(log(x)!)+%2F+x)
# https://www.wolframalpha.com/input/?i=limit+as+x+goes+to+infinity+(log(log(x)!)+%2F+(logx))
def num_1s_in_ints_le(N):
    """Returns the number of times digit 1 occurs in the decimal representation
         of all positive integers less than or equal to N.
    """
    
    if N == 0:
        return 0
    
    N_str = str(N)
    
    n_d_N = len(N_str) # number of digits in N
    n_d_p = 1          # number of digits in prefix
    n_d_s = n_d_N - 1  # number of digits in suffix
    
    res = 0
    
    # INVARIANT:
    #   n_d_s = n_d_N - n_d_p
    while n_d_s >= 0:
        
        N_prefix_str   = int( N_str[:n_d_p] )
        working_prefix = int( N_str[:n_d_p - 1] + "0" )
        
        while working_prefix < N_prefix_str:
            
            res += num_1s_in_int(working_prefix) * 10**n_d_s
            
            # add in the number of times digit 1 occurs
            # in all positive integers < 10**n_d_s, i.e.
            # in all positive integers that have at most
            # n_d_s number of digits in their representation
            
            if n_d_s > 0:
                res += 10**(n_d_s - 1) * n_d_s
            
            working_prefix += 1
        
        n_d_p += 1
        n_d_s -= 1
    
    res += num_1s_in_int(N)
    
    return res


# O(lg{N!}) time
# which is O(Nlg{N}) time
# according to WolframAlpha:
# https://www.wolframalpha.com/input/?i=limit+as+x+goes+to+infinity+(log(x!)+%2F+(x*logx))
def num_1s_in_ints_le_brute_force(N):
    # 1. Brute force version of num_1s_in_ints_le(N).
    # 2. Trivially correct.
    # 3. Used to further verify the efficient solution.
    
    res = 0
    for i in range(1, N+1):
        res += num_1s_in_int(i)
    return res


# O(lgN) time
def num_1s_in_int(N):
    """Returns the number of times digit 1 occurs in the decimal representation
         of N.
    """
    
    res = 0
    for digit in str(N):
        if digit == "1":
            res += 1
        # res += (digit == "1")
    return res


# DIRECTED TESTING


def _run_directed_tests():
    
    test_cases = [
                  (13,    6), # (N, expected output of solution(N))
                  (9,     1),
                  (99,    20),
                  (999,   300),
                  (9999,  4000),
                  (99999, 50000),
                  (12345, 8121)   ]

    for test_case in test_cases:
        
        N, expected_result = test_case
        
        actual_result = solution(N)
        
        # assert actual_result == expected_result
        print _get_result_string(N, actual_result, expected_result)


def _get_result_string(N, actual, expected):
    
    if actual == expected:
        description = " as expected"
    else:
        description = ", but was expecting {}".format(expected)
    
    return "solution({}) == {}{}".format(N, actual, description)


# RANDOM TESTING


def _run_this_many_random_tests(number_of_tests):
    
    number_of_failed_tests = 0
    
    for i in range(number_of_tests):
        
        test_passed, _, _, _, = _test_solution_once()
        
        if not test_passed:
            number_of_failed_tests += 1
    
    if number_of_failed_tests == 0:
        print "Passed all {} random tests! :)".format(number_of_tests)
    else:
        print "Failed {}/{} random tests. :(".format(number_of_failed_tests, 
                                                     number_of_tests)


import random


def _test_solution_once():
    
    N = random.randint(1, 10**5)
    
    expected_result = num_1s_in_ints_le_brute_force(N)
    actual_result   = solution(N)
    
    return (actual_result == expected_result, expected_result, actual_result, N)


if __name__ == "__main__":
    _run_directed_tests()
    _run_this_many_random_tests(100)