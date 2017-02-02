import sys
# import math # Jose: I don't think this was used after all

# Jose: since the code you gave me wasn't indented, I inferred the indentation in places where it was ambiguous
#       I always did this, inferring where I thought the correct indenation would be

def findBusiestPeriod(traffic):            # Jose: changed method name from noun to verb to indicate action 
    
    TIME, COUNT, TYPE = 0, 1, 2            # Jose: these are "named" indices into each traffic item
                                           #       I prefer using these instead of int literals because they convey more meaning
    
    traffic.sort(key=lambda item:item[TIME])
    #print(traffic)
    intialCountInMall = 100  # Jose: I am not sure why you set this to 100 instead of 0
                             #       also this var refers to the intial number of people in the mall
                             #       since this var and ppl_soFar both refer to the same idea
                             #       consider using the same nouns (either ppl or count) in both vars
                             #       This is a principle of readability: that similar things should be named similarly
                             #       For example, you can go with initialNumPpl and numPpl_soFar and maxNumPpl_soFar
                             #                    using ppl in all three variables signals that they are related, which they are
    
    n = len(traffic) # Jose: I added newlines to increase readability

    FIRST, LAST = 0, n-1 # Jose: "named" indeces to convey meaning
    
    startTimeStamp = traffic[FIRST][TIME] # Jose: aligned the var assingments
    endTimeStamp   = traffic[LAST][TIME]
    
    ppl_soFar     = intialCountInMall
    max_ppl_soFar = intialCountInMall # Jose: so max_ppl_soFar is set to 100 here and so is ppl_so_far, but I don't understand why they are not both just set to 0
                                      #       is it maybe to ward off against there being negative number of people inside the mall at one time???
                                      #       If so let me know :).
    
    # for i in range(n):
    for i, item in enumerate(traffic): # Jose: now you have access to both the index and the item
        
        if item[TYPE] == "Enter":      # Jose: in python there's no need to enclose conditions inside braces
            ppl_soFar += item[COUNT]   # Jose: adding spaces in ppl_soFar+=int(item[COUNT]) makes it more readable
        
        else:                          # Jose: item[COUNT] is already an int, no need to int(item[COUNT])
            ppl_soFar -= item[COUNT]

        # Jose: As you know, indentation matters in Python,
        #       so the entire next section should start at the same indentation level as if item[TYPE] == "Enter":
        
        if ppl_soFar > max_ppl_soFar:
            startTimeStamp = item[TIME]

            if i == LAST:
                endTimeStamp = item[TIME]
            else:
                endTimeStamp = traffic[i+1][TIME] # Jose: As you know, this is why you need the index in ln 29 lol

            max_ppl_soFar=ppl_soFar

    return [startTimeStamp, endTimeStamp]

#START
print( "Enter number of entries in traffic : " )
n = int( input() )
traffic = []

print( "Enter the traffic entries in form - timeStamp ppl type(enter/exit) : " ) # Jose: Cool, I like this form of input. I learned something new here lol.

for i in range(n):
    time, ppl, entryType = input().split()

    traffic.append([int(time), int(ppl), str(entryType)] )

#print(traffic)
print("Busiest time period in mall is ")
print( findBusiestPeriod(traffic) )