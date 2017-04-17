# courtesy of dose: https://www.interviewbit.com/profile/dose
# I helped him/her debug his/her code

# my own solution for merge_intervals was a disgrace: see merge_intervas_disgrace.py

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
      
      if len(intervals) <= 0:
        return [new_interval]
      
      res= []
      
    #   intervals.append(new_interval)
    #   # Sort list according to the start value x.start
    #   intervals.sort(key= lambda x:x.start)
      
      # lns 28 thru 34 are more efficient than and replace lns 23 thru 25,
      # exploit the fact that intervals is already sorted by start times
      i= 0
      while i < len(intervals) and intervals[i].start < new_interval.start:
          i+= 1
      # {intervals[:i].start <   new_interval.start}
      # { new_interval.start <= intervals[i:].start}
      intervals= intervals[:i] + [new_interval] + intervals[i:]
      
      res.append(intervals[0])
      
      for i in xrange(1, len(intervals)):
        # Check if previous interval end is higher than current interval start
        if res[-1].end >= intervals[i].start:
          res[-1].end = max(intervals[i].end, res[-1].end)
        else:
          res.append(intervals[i])
      return res