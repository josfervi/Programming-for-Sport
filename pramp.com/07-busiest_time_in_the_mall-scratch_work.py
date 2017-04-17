# doesn't handle case where people enter and exit at the same second

maintain a var that tracks the number of people in the mall

time   count   type         number_of_people
1      4       enter        4

3      3       exit         1

10     10      enter        11

14     20      enter        31

19      5      exit         26

between [time 14 and time 19] there were 31 people and this was the busiest period

# [(1, 0, xxxx)]<< you won't get a list item that says 0 people entered/exited the mall

mall_traffic= [(1, 4, "enter"), (3, 3, "exit")]

# sort mall_traffic by timestamp
TIME= 0
mall_traffic.sort(key= lambda x : x[TIME])

def findBusiestPeriod(mall_traffic):
   
   number_of_people= 0
   max_number_of_people_so_far= 0
   max_start= None
   max_end=   None
   
   LAST= len(mall_traffic) - 1 # mustn't be -1
   TIME=  0
   
   TIME_YEAR_ENDS_AT= ???? # UNIX TIME corresponding to DEC 31, YYYY 11:59:59 PM
   
   for idx, time, count, typ in enumerate(mall_traffic):
      
      sign= 1 if typ == "enter" else -1
      number_of_people+= (sign * count)
      
#       if typ == "enter":  number_of_people+= count
#       elif typ == "exit": number_of_people-= count
#       else: raise "error"
      
   
      if number_of_people > max_number_of_people_so_far:
         max_number_of_people_so_far= number_of_people
         max_start= time
         if idx == LAST:
            max_end= TIME_YEAR_ENDS_AT
         else:
            max_end= mall_traffic[idx+1][TIME]
    
    return [max_start, max_end]