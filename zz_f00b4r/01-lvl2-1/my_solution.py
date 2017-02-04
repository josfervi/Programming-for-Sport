# Submission: SUCCESSFUL. Completed in: 1 hr, 55 mins, 36 secs / 72 hours

# INDEX
#
# SOLUTION
# - def answer(nums, target)
#
# TESTING
# - def run_tests()        # runs directed tests, then calls run_random_tests()
# - def run_random_tests() # calls test_answer_once() NUMBER_OF_RADOM_TEST_CASES times
# - def test_answer_once() # runs one random test on answer(nums, target)
# - printFailString(...)   # useful for differentiating between false fails and real fails
# 
# random testing helped me catch and fix two bugs,
# furthermore, using printFailString(...) I observed that all "failing" test cases
#              were probably false fails

PAIR_NOT_FOUND = [-1,-1]

''' Given a list of positive integers, nums,
    and a positive integer, target,
    return the lexicographically smallest
    index-pair [idx, jdx] s.t.
    sum( nums[idx : jdx+1] ) == target.
    If no such pair exists,
    return [-1, -1] '''
def answer(nums, target):
    
    if len(nums) == 0:
        return PAIR_NOT_FOUND
    
    idx, jdx = 0, -1
    sum_soFar = 0
    
    # INVARIANT: sum_soFar = sum( nums[idx : jdx+1] ) before the beginning of each iteration
    for jdx, num in enumerate(nums):
        
        if num == target:
            return [jdx, jdx]
            
        if num > target:
            idx = jdx + 1
            sum_soFar = 0
            continue
        
        # { num < target }
        sum_soFar += num
        
        if sum_soFar == target:
            return [idx, jdx]
        
        if sum_soFar <  target:
            # let sum_soFar grow in the next iteration
            continue
        
        # { sum_soFar > target }
        # move idx up until sum_soFar <= target
        while idx <= jdx and sum_soFar > target:
            sum_soFar -= nums[idx]
            idx += 1
        
        # { sum_soFar <= target }
        
        if sum_soFar == target:
            return [idx, jdx]
    
    return PAIR_NOT_FOUND

# TESTS

# def run_tests():
    
#     # Directed tests
#     print answer([4,3, 5,7,8], 12) == [0,2]
#     print answer([4,3,10,2,8], 12) == [2,3]
#     print answer([1,2, 3,4],   15) == PAIR_NOT_FOUND
    
#     # found and simplified regressions through random testing
#     print answer([2,1], 1) == [1,1]
#     print answer([1],   1) == [0,0] 

#     run_random_tests()

# from random import randint, choice

# NUMBER_OF_RADOM_TEST_CASES = 100

# def run_random_tests():
    
#     number_of_failed_tests = 0
    
#     for test_no in range(NUMBER_OF_RADOM_TEST_CASES):
        
#         (test_passed, nums, target, actual_result, expected_result) = test_answer_once()
#         if not test_passed:
#             printFailString(test_no, nums, target, actual_result, expected_result)
#             number_of_failed_tests += 1
    
#     if number_of_failed_tests == 0:
#         print "Passed all {0} random test cases! :)".format(NUMBER_OF_RADOM_TEST_CASES)
#     else:
#         print "Failed {0}/{1} random test cases. :(".format(number_of_failed_tests, NUMBER_OF_RADOM_TEST_CASES)

# def test_answer_once():
    
#     length = randint(1,100)
    
#     nums = [None]*length
    
#     for i in range(length):
#         nums[i] = randint(1,100)
    
#     found = choice([True, False])
    
#     if not found:
#         target = sum(nums) + 1
        
#         actual_result   = answer(nums, target)
#         expected_result = PAIR_NOT_FOUND
#         test_passed     = actual_result == expected_result
#         return (test_passed, nums, target, actual_result, expected_result)
    
#     # found is True
            
#     idx_ = randint(   0, length-1)
#     jdx_ = randint(idx_, length-1)
    
#     target = sum(nums[idx_ : jdx_+1])
    
#     # Fcn will report a false negative (i.e. a false fail)
#     # if there actually exist lexicographically smaller
#     # [idx, jdx] s.t. sum(nums[idx : jdx+1]) == target.
#     # 
#     # To differentiate between such false fails and actual fails,
#     # I'll manually recheck every fail to determine if it was a false fail or a real fail.
#     actual_result   = answer(nums, target)
#     expected_result = [idx_, jdx_]
#     test_passed     = actual_result == expected_result
#     return (test_passed, nums, target, actual_result, expected_result)

# def printFailString(test_no, nums, target, actual_result, expected_result):
    
#     got_idx, got_jdx = actual_result
#     got_sum = sum(nums[got_idx : got_jdx+1])
    
#     exp_idx = expected_result[0]
#     if got_sum == target and got_idx < exp_idx:
#         context = " Probaly a false fail." # because got_sum == sum(nums[{0}..{1}]) == {2} == {3} == target and got_result is lexicographically smaller than exp_result".format(got_idx, got_jdx, got_sum, target)
#     else:
#         context = " Probably a real fail."
    
#     print "========================================"
#     print "Failed test {0}:".format(test_no)
#     print " Context: "      + context
#     print "  nums:     {0}".format(nums)
#     print "  target:   {0}".format(target)
#     print "  got:      {0}".format(actual_result)
#     print "  expected: {0}".format(expected_result)
#     print "========================================"
#     print ""

# if __name__ == "__main__":
#     run_tests()