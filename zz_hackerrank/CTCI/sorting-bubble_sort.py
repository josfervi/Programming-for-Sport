n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def bubble_sort(nums):
  
  n = len(nums)
  
  num_swaps_total = 0
  num_swaps_this_pass = 0
  
  num_passes = 0
  
  while num_passes < n:
    
    # on the jth pass the last j
    # numbers are exactly where
    # they need to be
    for i in range(1, n-num_passes):
      
      if a[i-1] > a[i]:
        # swap
        a[i-1], a[i] = a[i], a[i-1]
        num_swaps_this_pass += 1
    
    num_swaps_total += num_swaps_this_pass
    num_passes += 1
    
    if num_swaps_this_pass == 0:
      return (nums, num_swaps_total)
    
    num_swaps_this_pass = 0
  
  return (nums, num_swaps_total)

sorted_nums, num_swaps = bubble_sort(a)

print "Array is sorted in {} swaps.".format(num_swaps)
print "First Element: {}".format(sorted_nums[0])
print "Last Element: {}".format(sorted_nums[-1])
