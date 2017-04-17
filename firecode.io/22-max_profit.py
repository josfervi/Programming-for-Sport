def max_profit(nums):
    
    if not nums:
        return 0
    
    max_profit_soFar = 0
    prev_num = nums[0]
    for num in nums[1:]:
        max_profit_soFar += max(num-prev_num, 0)
        prev_num = num
    
    return max_profit_soFar