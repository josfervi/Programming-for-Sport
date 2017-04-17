# Pramp >> Island Count asked by Greg
# https://www.pramp.com/question/yZm60L6d5juM7K38KYZ6

# (I asked Greg the arr[i] = i question)

#       0 1 2 3 4 5
#
#       # # # # #
# 0   # 0 1 0 1 0
# 1   # 0 0 1 1 1
# 2   # 1 0 0 1 0
# 3   # 0 1 1 0 0
# 4   # 1 0 1 0 1
# 5

# R - number of rows of m
# C - number of cols of m
#
# O(R*C) time
# O(R+C) space
#        the queue holds a growing wave of cells
#        that cannot get larger than the boundary
#        of the island with the largest island
def countIslands(m)
   
   if m == []
      return 0
   end
   
   num_rows = m.length
   num_cols = m[0].length
   
   island_count = 0
   
   0.upto (num_rows-1) do |r|
      0.upto (num_cols-1) do |c|
         
         if m[r][c] == 1
            island_count += 1
            markIsland(m, r, c)
         end
      end
   end
   
   return island_count
end

def markIsland(m, r, c)
   
   if m == []
      return 0
   end
   
   num_rows = m.length
   num_cols = m[0].length
   
   m[r][c] = 2
   island_queue = [ [r,c] ] # ruby does not have tuples
   
   while !island_queue.empty? do
      
      r,c = island_queue.shift
      
      # up
      if r-1 >= 0 && m[r-1][c] == 1
         m[r-1][c] = 2
         island_queue.unshift([r-1,c])
      end
      # down
      if r+1 < num_rows && m[r+1][c] == 1
         m[r+1][c] = 2
         island_queue.unshift([r+1,c])
      end
      # left
      if c-1 >= 0 && m[r][c-1] == 1
         m[r][c-1] = 2
         island_queue.unshift([r,c-1])
      end
      # right
      if c+1 < num_cols && m[r][c+1] == 1
         m[r][c+1] = 2
         island_queue.unshift([r,c+1])
      end
   end
end

# TEST
#       # # # # #
# 0   # 0 1 0 1 0
# 1   # 0 0 1 1 1
# 2   # 1 0 0 1 0
# 3   # 0 1 1 0 0
# 4   # 1 0 1 0 1

m = \
[ [0, 1, 0, 1, 0], \
  [0, 0, 1, 1, 1], \
  [1, 0, 0, 1, 0], \
  [0, 1, 1, 0, 0], \
  [1, 0, 1, 0, 1]    ]

puts countIslands(m) == 6

# THE IMPORTANCE OF MARKING AS SOON AS POSSIBLE

# instead of a) marking a cell after you dequeue its coords from the queue
# you should b) mark the cell before you enqueue its corrds into the queue
#
# this prevents you from putting the same cell in the queue multiple times

# in the followint examples
# .   represents a cell that is part of an island / is an island
# ,   represents a cell that's been marked
# 1-9 represent a cell's position in the queue
#
# ,1 means that a cell is marked and is first in the queue
# if there is a 2 but not a 1 the cell with the 2 is first in the queue

# 2x2 matrix example using a)
# 
# . .  =>  1 .   =>  , 2    =>  , 2   =>  , ,   =>  , ,   =>  , ,
# . .  =>  . .   =>  1 .    =>  , 3   =>  , 34  =>  , ,4  =>  , ,
# 
# notice how cell at (1,1) was enqueued twice

# b) 
#    dequeue a cell's coords
#    mark it
#    for each unmarked island neighbor cell
#        mark the neighbor cell
#        enqueue the neighbor cell's coords
# same 2x2 matrix example using b)
# 
# . .  =>  ,1 .  =>  ,  ,2  =>  , ,2  =>  , ,   =>  , ,
# . .  =>  .  .  =>  ,1 .   =>  , ,3  =>  , ,3  =>  , ,