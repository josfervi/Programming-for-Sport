# incorrect

import copy

def chipMoving(grid):
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    # min_cost[r][c] := the min cost to get to tile at pos r,c
    min_cost = [[None]*num_cols for _ in range(num_rows)]
    
    # move[r][c] := the move taken to get to tile at pos r,c
    move = [[None]*num_cols for _ in range(num_rows)]
    
    for r in range(num_rows):
        for c in range(num_cols):
            
            if r == 0 and c == 0:
                min_cost[r][c] = 0
                move[r][c] = None
                continue
            
            if r == 0:
                
                # moving along the top row, always going right
                
                min_cost[r][c] = min_cost[r][c-1] + grid[r][c]
                move[r][c] = 'right'
                continue
            
            if c == 0:
                
                # moving along the left column, always going down
                
                min_cost[r][c] = min_cost[r-1][c] + grid[r][c]
                move[r][c] = 'down'
                continue
            
            # try going down from above
            cost_to_come_from_above = (
                    
                    min_cost[r-1][c] +
                    (10 if move[r-1][c] == 'right' else 0) +
                    grid[r][c]
            )
            
            # try going right from the left
            cost_to_come_from_the_left = (
                    
                    min_cost[r][c-1] +
                    (10 if move[r][c-1] == 'down' else 0) +
                    grid[r][c]
            )
            
            if cost_to_come_from_above < cost_to_come_from_the_left:
                
                # move down from the tile above you to
                # to achieve the min cost of getting to tile at r,c
                
                min_cost[r][c] = cost_to_come_from_above
                move[r][c] = 'down'
            
            elif cost_to_come_from_above == cost_to_come_from_the_left:
                
                # you can achieve the min cost of getting to tile at r,c
                # by either
                # coming in from above
                # or
                # coming in from the left
                
                min_cost[r][c] = cost_to_come_from_above
                move[r][c] = 'either'
                
            else:
                
                # move right from the tile to your left to
                # achieve the min cost of getting to tile at r,c
                
                min_cost[r][c] = cost_to_come_from_the_left
                move[r][c] = 'right'
    
    return min_cost[num_rows-1][num_cols-1]
            
#
grid = [[4,11,6,16,6,9,3,2,10,14], 
 [1,7,8,11,16,3,18,13,5,12], 
 [10,12,10,2,15,0,18,11,13,7], 
 [14,15,15,15,9,5,11,11,7,4], 
 [5,9,15,19,4,4,11,4,14,8], 
 [5,5,15,2,15,15,14,10,19,19], 
 [8,9,2,3,18,12,15,10,10,3], 
 [8,2,1,11,4,3,16,7,8,13], 
 [17,2,17,10,17,13,16,14,8,5], 
 [10,4,9,3,13,10,5,4,3,10]]

res = chipMoving(grid)
print res
print res == 144