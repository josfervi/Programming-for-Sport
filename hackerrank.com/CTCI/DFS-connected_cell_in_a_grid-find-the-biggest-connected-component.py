FILLED_LABEL = 1

def get_size_of_biggest_connected_component(grid):
  
  n = len(grid)
  m = len(grid[0])
  
  current_label = -1
  size_of_biggest_cc_soFar = 0
  
  for r in range(n):
    for c in range(m):
      
      if grid[r][c] == FILLED_LABEL:
        size_of_current_cc = label_connected_component(grid, (r,c), current_label)
        current_label -= 1
        size_of_biggest_cc_soFar = max(size_of_biggest_cc_soFar, size_of_current_cc)
  
  return size_of_biggest_cc_soFar

from collections import deque

def label_connected_component(grid, pos, label):
  
  g = grid
  n = len(g)
  m = len(g[0])
  FL = FILLED_LABEL
  r, c = pos
  
  assert g[r][c] == FILLED_LABEL
  
  queue = deque([])
  
  size_of_cc = 0
  
  g[r][c] = label
  queue.append( (r,c) )
  
  while queue:
    
    r, c = queue.popleft()
    size_of_cc += 1
    
    # up
    if r-1 >= 0 and g[r-1][c] == FL:
      g[r-1][c] = label
      queue.append( (r-1, c) )
    
    # down
    if r+1 < n and g[r+1][c] == FL:
      g[r+1][c] = label
      queue.append( (r+1, c) )
    
    # left
    if c-1 >= 0 and g[r][c-1] == FL:
      g[r][c-1] = label
      queue.append( (r, c-1) )
    
    # right
    if c+1 < m and g[r][c+1] == FL:
      g[r][c+1] = label
      queue.append( (r, c+1) )
    
    # up left
    if r-1 >= 0 and c-1 >= 0 and g[r-1][c-1] == FL:
      g[r-1][c-1] = label
      queue.append( (r-1, c-1) )
    
    # up right
    if r-1 >= 0 and c+1 < m and g[r-1][c+1] == FL:
      g[r-1][c+1] = label
      queue.append( (r-1, c+1) )
    
    # down left
    if r+1 < n and c-1 >= 0 and g[r+1][c-1] == FL:
      g[r+1][c-1] = label
      queue.append( (r+1, c-1) )
    
    # down right
    if r+1 < n and c+1 < m and g[r+1][c+1] == FL:
      g[r+1][c+1] = label
      queue.append( (r+1, c+1) )
  
  return size_of_cc

def get_biggest_region(grid):
    return get_size_of_biggest_connected_component(grid)

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
