# DONE

# O(n^2) time
# O(1) time
def pancakeSort(arr):
  
  n = e = len(arr)
  
  # INVARIANT
  #   arr[e:] is/are in its/their final sorted position
  while e > 1:
    k = 0
    next_max = arr[0]
    for i, val in enumerate(arr[1:e], 1):
        if val > next_max:
            next_max = val
            k = i
    
    # use flip to move the kth val (next_max)
    # into the e-1th position
    
    if k != e-1:
      # bring the kth val (next_max) to the 0th position
      flip(arr, k+1)
      
      # bring next_max (at 0th position) to the e-1th position
      flip(arr, e)
    
    e -= 1
  
  # e == 1
  # arr[1:] is/are in its/their final sorted position
  # arr[0] cannot be in any other position than the 0th position
  # arr is sorted
  return arr
  
def flip(arr, k):
  assert k <= len(arr)
  
  if k <= 1:
    return
  
  s, e = 0, k-1
  while s < e:
    arr[s], arr[e] = arr[e], arr[s]
    s += 1
    e -= 1
  return arr


arr = [1, -1, 5, 4, 7, 3, 2, 6]
print pancakeSort(arr)


'''
aside:

reverse(i, j) = reverse(0, j+1) then reverse(0, j-i+1) then reverse(0, j+1)
              = flip j+1             flip j-i+1             flip j+1

0 1 2 3 4 5 6 7 8 9 0 1
    i     j 
a b c d e f g h i j k l

f e d c b a # flip the first j+1 elements

c d e f b a # flip the first j-i+1 elements

a b f e d c # flip the first j+1 elements

0 1 2 3 4 5 6 7 8 9 0
      i         j
a b c d e f g h i j k
i h g f e d c b a j k # after flipping the first j+1
d e f g h i c b a j k # after flipping the first j-i+1
a b c i h g f e d j k # after flipping the first j+1
      i         j
'''