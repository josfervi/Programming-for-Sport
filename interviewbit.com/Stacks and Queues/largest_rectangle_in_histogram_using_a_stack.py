class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, heights):
        
        n = len(heights)
        
        # stack will store a triplet of
        #   - height
        #   - idx
        #   - index of nearest smaller or left blocking idx
        #       because the bar at left blocking idx is
        #       smaller than height and blocks its leftward
        #       expansion
        stack = []
        
        HEIGHT  = 0
        IDX     = 1
        TOP = -1
        
        max_area_soFar = 0
        
        for idx, curr_height in enumerate(heights):
            
            # idx is the right blocking idx
            R = idx-1
            while stack and stack[TOP][HEIGHT] >= curr_height:
                
                height, _, L_p = stack.pop()
                # L_p is the left blocking idx
                L = L_p + 1
                area = height * (R-L+1)
                max_area_soFar = max(max_area_soFar, area)
            
            # if you make the > on line 27 a >= instead,
            # you can get rid of lines 38 - 43
            # I HAVE DONE THIS
            # if stack and stack[TOP][HEIGHT] == curr_height:
            #     _, _, L_p = stack.pop()
            #     stack.append( (curr_height, idx, L_p) )
            #     # subsequent items may look to this idx for
            #     # their left_blocking_idx
            #     continue
            
            left_blocking_idx = stack[TOP][IDX] if stack else -1
            stack.append( (curr_height, idx, left_blocking_idx) )
        
        # flush out the stack
        # n is the right blocking idx
        R = n - 1
        while stack:
            
            height, _, L_p = stack.pop()
            # L_p is the left blocking idx
            L = L_p + 1
            area = height * (R-L+1)
            max_area_soFar = max(max_area_soFar, area)
        
        return max_area_soFar


# heights = [ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]
# sol = Solution()
# print sol.largestRectangleArea(heights) == 348