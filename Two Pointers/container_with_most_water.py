class Solution:
  # @param A : list of integers
  # @return an integer
  def maxArea(self, heights):
    
    N= len(heights)
    if N < 2: return 0
    
    max_area= -1
    
    left=    0
    right= N-1
    
    while left<right:
      potential_area= (right-left) * min( heights[left], heights[right] )
      max_area=       max( max_area, potential_area )
      
      if   heights[left ] < heights[right]: left+=  1
      elif heights[right] < heights[left ]: right-= 1
      else:
        left+=  1
        right-= 1
    
    return max_area