# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        
        sorted_intervals= sorted(intervals, key= lambda i : i.start)
        
        merged_intervals= [ ] # accumulates the result
        current_merged_interval=  sorted_intervals[0] # the current merged interval
        
        for interval in sorted_intervals[1:]:
            
            # { previous_iteration{interval.start} <= current_iteration{interval.start} }
            # { merged_interval.start <= interval.start
            
            if interval.start <= current_merged_interval.end:
                # intervals overlap
                current_merged_interval.end= max(interval.end, current_merged_interval.end)
               
            else:
                # intervals do not overlap
                merged_intervals.append(current_merged_interval)
                current_merged_interval= interval
        
        merged_intervals.append(current_merged_interval)
        
        return merged_intervals