# O(n^2) time
# O(1)   extra space
def bubble_sort(nums):
    
    N= len(nums)
    
    # INVARIANT: nums[:i] is unsorted
    #            nums[i:] is sorted and in its final position
    
    for i in range(N, 0, -1):
        for j in range(1, i):
            if nums[j-1] > nums[j]:
                # swap
                nums[j-1], nums[j] = nums[j], nums[j-1]
    
    # {nums[:1] is unsorted}
    # {nums[1:] is sorted and in its final position}
    # =>
    # {nums is sorted}
    
    return nums