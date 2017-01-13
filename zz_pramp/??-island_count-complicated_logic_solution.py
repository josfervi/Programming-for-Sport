a probably correct non DFS, non BFS solution to the counting islands problem ( counting the number of connected components in a binary image)
that can be easily reworked into a
O(n*m) time
O(1) working space
solution

however, this solution is very hard to read / understand
because of the heavily nested logic necessary

the DFS/BFS solution is much easier to read and understand

def countIslands(board):
    
    num_rows= len(board)
    num_cols= len(board[0])
    
    board_label= [[None]*num_cols for _ in range(num_rows)] # see footnote 1
    
    island_count= 0 # the island count to the best our running knowledge,
                    # converges on the correct value at the end of execution
    
    current_label= 0 # how many unique islands we think we've seen
                     #
                     # Sometimes, as we 'uncover' more of the board,
                     # two board regions that we thought were two seperate islands
                     # turn out to actually be one island.
                     # When this happens, we decrement island_count by 1
    
    for r in range(num_rows):
        for c in range(num_cols):
            
            if board[r][c] == 1:
                
                # update stuff
                label_above_me, label_on_my_left = None, None
                if r - 1 >= 0:
                    label_above_me=   board_label[r-1][c]
                if c - 1 >= 0:
                    label_on_my_left= board_label[r][c-1]
                
                # label_above_me can be None becuase
                # 1) r-1 < 0 or
                # 2) board[r-1][c] == 0 and thus board_label[r-1][c] == None
                
                if label_above_me and label_on_my_left:
                    
                    # check for a conflict
                    
                    if label_above_me != label_on_my_left:
                        
                        label_on_my_NW= board_label[r-1][c-1]
                        
                        if label_on_my_NW:
                            pass
                        else:
                            island_count-= 1
                        
                    board_label[r][c]= label_above_me
                        
                elif label_above_me:
                    board_label[r][c]= label_above_me
                    
                elif label_on_my_left:
                    board_label[r][c]= label_on_my_left
                    
                else:
                    current_label+=    1
                    board_label[r][c]= current_label
                    
                    island_count+= 1
    return island_count
                
                    
matrix1= \
[ [0, 0, 0, 0, 1, 1],
  [0, 0, 1, 1, 1, 1],
  [0, 0, 1, 1, 1, 1],
  [0, 1, 1, 1, 0, 0] ]
  
print countIslands(matrix1) == 1

matrix2= \
[ [0, 0, 0, 0, 1, 1],
  [0, 0, 1, 1, 1, 1],
  [0, 0, 1, 1, 1, 1],
  [0, 1, 1, 1, 0, 0],
  [0, 1, 0, 0, 1, 0],
  [0, 1, 1, 1, 1, 1] ]

print countIslands(matrix2) == 1

spiral_island= \
[ [1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 1],
  [1, 0, 0, 1, 0, 1],
  [1, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1] ]

print countIslands(spiral_island) == 1

# footnotes
# 
# 1) [None]*2
#    
#    creates
#    
#    [None, None]
#    
#    
#    [[None]*2 for _ in range(3)]
#    
#    is a one-liner that uses list-comprehension for creating
#    
#    [ [None, None],
#      [None, None],
#      [None, None], ]