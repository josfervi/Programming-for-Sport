# Exploring the space of solutions:
# 
# If input array is not sorted,
# use a set for O(1) membershipt testing*.
# *Assuming we have a good underlying hash function.
# This approach is O(N) time, O(N) extra space.
#
# If input were alreay sorted, we could use
# a more efficient O(N) time, O(!) extra space
# two-pointer approach.
# 
# If we cannot afford O(N) extra space, and our
# input array is not sorted, we can do in-place
# iterative heapsort. This will take O(NlgN) time,
# and O(1) extra space. Once we've sorted the input
# array, then we can use the O(N) time, O(1) extra
# space two-pointer approach. Overall, we'd have a
# O(NlgN) time, O(1) extra space solution.


def two_sum_to_42(nums):
    return two_sum(nums, 42)


# O(N) time where N == len(nums)
# O(N) extra space
def two_sum(nums, target_sum):
    
    nums_seen = set()
    
    for num in nums:
        
        complement = target_sum - num
        if complement in nums_seen:
            return True
        
        nums_seen.add(num)
    
    return False


# TESTS


def test_two_sum_to_42_with_sorted_input():
    """
    Assumming the given expected result is correct,
        prints True for each passed test, and 
        prints False for each failed test.
    """
    
          # actual result                         expected result
    print two_sum_to_42([])                    == False
    print two_sum_to_42([42])                  == False
    print two_sum_to_42([21])                  == False
    print two_sum_to_42([1,21])                == False
    print two_sum_to_42([20,21])               == False
    print two_sum_to_42([1,2,6,9,10,23,27])    == False
    print two_sum_to_42([1,2,6,9,10,19,23,27]) == True


def test_two_sum_to_42():
    """
    Assumming the given expected result is correct,
        prints True for each passed test, and 
        prints False for each failed test.
    """
              # actual result                         expected result
    print two_sum_to_42([21,1])                == False
    print two_sum_to_42([21,20])               == False
    print two_sum_to_42([1,23,9,2,10,6,27])    == False
    print two_sum_to_42([1,2,23,6,9,10,27,19]) == True
    print two_sum_to_42([7,99,20,-1,59,29,42]) == False
    print two_sum_to_42([3,1,0,21,12,-49,21])  == True
    print two_sum_to_42([48, 3, 29, 100, -58]) == True


test_two_sum_to_42_with_sorted_input()
test_two_sum_to_42()