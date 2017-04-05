def selection_sort(nums):
    
    n = len(nums)
    
    sorted_up_to = 0
    
    # nums[:sorted_up_to] is sorted
    while sorted_up_to < n:
        
        min_idx = get_min_idx(nums, sorted_up_to)
        
        nums[sorted_up_to], nums[min_idx] = nums[min_idx], nums[sorted_up_to]
        
        sorted_up_to += 1
        
    return nums

def get_min_idx(nums, sorted_up_to):
    ''' Returns the idx (w.r.t nums) and the value
           of the minimal element of
           nums[sorted_up_to:].
    '''
    
    n = len(nums)
    
    if sorted_up_to >= n:
        return None
    
    min_soFar_idx = sorted_up_to
    min_soFar = nums[min_soFar_idx]
    for idx, num in enumerate(nums[sorted_up_to+1:]):
        if num < min_soFar:
            min_soFar = num
            min_soFar_idx = sorted_up_to+1+idx
    
    return min_soFar_idx
        
        