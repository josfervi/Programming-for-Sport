# i -> r
# j -> c


# dp[0][0] = 1
# dp[r][c] = dp[r-1][c] + dp[r][c-1] if r >= c
#          = 0                       if r <  c


# O(n**2) time
# O(n**2) space
def numOfPathsToDest(n):
  
  dp = [ [None]*n for _ in range(n) ]
  
  dp[0][0] = 1
  
  for r in range(1, n):
    for c in range(r+1):
      # r >= c
                 # r >= c-1                      # r-1 >= 0 because r >= 1
                 # left                          # down
      dp[r][c] = (dp[r][c-1] if c-1>=0 else 0) + (dp[r-1][c] if r-1>=c else 0)
                 # make sure it's inbounds       # make sure it is valid
  return dp[n-1][n-1]


import copy


# O(n**2) time
# O(n) space
def numOfPathsToDest_less_mem(n):
  
  if n == 1:
    return 1
  
  prev_row = [None]*n
  prev_row[0] = 1        # prev_row    == dp[0]
  current_row = [None]*n # current_row == dp[1]
  
  for r in range(1, n):
    for c in range(r+1):
      
      # r >= c
      
      # prev_row    == dp[r-1]
      # current_row == dp[r]
      
      current_row[c] = (current_row[c-1] if c-1>=0 else 0) + (prev_row[c] if r-1>=c else 0)
    
    # want prev_row to become current_row
    # current_row becomes prev_row, not because it should
    #   become prev_row specifically, but because current_row needs to be a
    #   a different list than prev_row
    # the easiest way to achieve this is to swap prev_row and current_row
    prev_row, current_row = current_row, prev_row

  current_row = prev_row
  return current_row[n-1]


# TESTS
print numOfPathsToDest(1) == 1
print numOfPathsToDest(2) == 1
print numOfPathsToDest(3) == 2
print numOfPathsToDest(4) == 5
print numOfPathsToDest(5) == 14
print numOfPathsToDest(7) == 132
print
print numOfPathsToDest_less_mem(1) == 1
print numOfPathsToDest_less_mem(2) == 1
print numOfPathsToDest_less_mem(3) == 2
print numOfPathsToDest_less_mem(4) == 5
print numOfPathsToDest_less_mem(5) == 14
print numOfPathsToDest_less_mem(7) == 132
