Jose
Rasmi

https://www.pramp.com/question/3QnxW6xoPLTNl5jX5Lg1

# Implement a meeting planner that can schedule meetings between two persons at a time.

# Time is represented by Unix format (also called Epoch) - a positive integer holding the seconds since January 1st, 1970 at midnight. 

# Planner input:

# dur - Meeting duration in seconds (a positive integer).
# timesA, timesB - Availability of each person, represented by an array of arrays.
# Each sub-array is a time span holding the start (first element) and end (second element) times.
# You may assume that time spans are disjointed.
# Planner output:

# Array of two items - start and end times of the planned meeting, representing the earliest opportunity for the two persons to meet for a dur length meeting.
# If no possible meeting can be scheduled, return an empty array instead.
# Design and implement an efficient solution and analyze its runtime and space complexity.

dur (pos int)
timesA = [ [1,2], [3,4], [5,6], [10,20] ]
timesB=  [ [2,3], [5,8] ]

I want to find one duration in timesA
that overlaps with another duration in timesB
and their overlap >= dur

def schedule_meeting(timesA, timesB, dur):
   
   i, j = 0, 0
   
   START_TIME= 0
   STOP_TIME=  1
   
   while i < len(timesA) and j < len(timesB):
      
      overlap= overlap(timesA[i], timesB[j])
      
      overlap_dur= overlap[STOP_TIME] - overlap[START_TIME]
      
      if overlap_dur >= dur:
         earliest_start_time= overlap[START_TIME]
         
         return [earliest_start_time, earliest_start_time + dur]
      
      
      # increment i or j appropriately
      #
      # I believe both strategies work
      # 
      # Strategy 1:
      #   increment i if timesA[i][STOP_TIME] <= timesB[j][STOP_TIME]
      #   increment j otherwise
      # Strategy 2:
      #   increment i if timesA[i+1][START_TIME] <= timesB[j+1][START_TIME]
      #   increment j otherwise
    
    # ignore thisvvvvv
    #   if overlap_dur == 0:
    #      #   |event1|      |event2     |
    #      # --+------+------+-----------+
    #      #   ^             ^
    #      if timesA[i][START_TIME] < timesB[j][START_TIME]:
    #         i+= 1
    #      else:
    #         j+= 1
    #   else:
         
         
   
   return -1



def overlap( event1, event2 ):
   START_TIME= 0
   END_TIME= 1

   start_time1, stop_time1 = event1
   start_time2, stop_time2 = event2
   
#   if start_time2 <= start_time1 <= stop_time2:
#       return [start_time1, min(stop_time1, stop_time2)]
   
#   elif start_time1 <= start_time2 <= stop_time1:
#       return [start_time2, min(stop_time2, stop_time1)]
   
#   return [0,0]
    
    overlap= [ max(start_time1, start_time2),
               min(stop_time1,  stop_time2)   ]
   
    if overlap[START_TIME] >= overlap[STOP_TIME]:
        return None
    return overlap
   #                 overlap starts here
   #                 v
   # -------+--------+-------+----------
   #        st2      st1     stopt2
   
# A = [10, 13], [24, 30]
# B = [11, 14], [26, 32]

#
# overlap(A[0],B[0]) == [11,13]
#
# overlap(A[0], B[1]) == None
#
   
   dur = 2 hrs
   
A= [10, 12], [14, 16]
B= [11, 17]
   
   A[0], B[0] they overlap for 1 hour, it's not enough!'
   A[1], B[0] they overlap for 2 hours, it's enough time'