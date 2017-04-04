# If input array is sorted,
# use a two pointer approach.


def two_sum_to_42(nums):
    return two_sum(nums, 42)


# O(N) time where N == len(nums)
# O(1) extra space
def two_sum(nums, target_sum):
    """
    :type nums: List[int]
      PRECONDITION: nums is sorted
    :type target: int
    :rtype: bool (one of True, False)

    Returns True if there exists two
        elements in numbers that add up
        to target_sum.
        Otherwise, returns False.
    """

    l, r = 0, len(nums)-1

    # INVARIAT:
    #   The sum of any pair taken
    #   from nums[:l], nums[r+1:]
    #   is not equal to target_sum.

    while l<r:

        curr_sum = nums[l] + nums[r]

        if curr_sum < target_sum:
            # Our current sum is too small.
            # Make it bigger (or at least
            # non-decreasing) in the next
            # iteration.
            l += 1
        elif curr_sum == target_sum:
            return True
        else: # curr_sum > target_sum
            # Our current sum is too big.
            # Make it smaller (or at least
            # non-increasing) in the next
            # iteration.
            r -= 1

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


test_two_sum_to_42_with_sorted_input()