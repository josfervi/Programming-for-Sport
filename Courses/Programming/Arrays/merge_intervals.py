# This code is a disgrace :( lol

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        
        if intervals == []:
            return [new_interval]

        last_interval= intervals[-1]
        if last_interval.start <= new_interval.start:
            if new_interval.start <= last_interval.end:
                merged_interval= Interval( min(new_interval.start, last_interval.start),
                                           max(new_interval.end,   last_interval.end)   )
                return intervals[:-1] + [merged_intervals]
            else:
                merged_interval= new_interval
                return intervals + [merged_interval]
        
        i= 0
        
        # let b/s denote "before or at the same time as/that"
        
        # invariant:
        # [english]     ea. interval in intervals[:i]  starts         b/s new_interval starts
        # [math   ] for ea. interval in intervals[:i], interval.start <=  new_interval.start
        
        interval= intervals[i]
        # TO DO: improvement: do a binary search
        while interval.start <= new_interval.start:
            i+= 1
            interval= intervals[i]
        
        # { intervals[:i] is the largest subset of intervals whose intervals each start b/s new_interval }
        
        f_o= i # (loosely) first overlap
        l_o= i # (loosely) last  overlap
        
        # invariant:
        # ea. interval in intervals[f_o : l_o] overlaps new_interval
        
        if i != 0:
            # there exists at least one interval that starts before new_interval
            # in that case the interval that starts immediately before new_interval may overlap new_interval
            left= i-1
            left_interval= intervals[left]
            if new_interval.start <= left_interval.end:
                # the interval that starts immediately before new_interval does overlap new_interval
                f_o= left= i-1
        
        # { interval == intervals[l_o] == intervals[i]}
        # { ea. interval in intervals[i:] starts after new_interval starts }
        # { any interval in intervals[i:] that starts b/s new_interval ends overlaps  new_interval
        
        # invariant:
        # ea. interval in intervals[i:l_o] starts after new_interval starts and
        #                                  starts  b/s  new_interval ends
        
        while interval.start <= new_interval.end:
            l_o+= 1
            interval= intervals[l_o]
        
        # intervals[f_o : l_o] is the largest subset of intervals whose intervals each overlap new_interval
        
        no_overlaps= f_o == l_o
        merged_interval= new_interval if no_overlaps else Interval( min(new_interval.start, intervals[f_o].start),
                                                                    max(new_interval.end,   intervals[l_o-1].end)  )
        
        return intervals[ : f_o] + [merged_interval] + intervals[l_o : ]    
        
        
