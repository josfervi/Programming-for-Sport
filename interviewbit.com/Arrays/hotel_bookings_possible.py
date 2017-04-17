# hotel is more efficient than hotel

# hotel has side effects:
#  - mutates arrive and depart
# the method can be easily modified to have no side effects

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    
    def hotel0self, arrive, depart, K):
        
        assert len(arrive) == len(depart)
        
        N= len(arrive)
        
        if N <= K: return True
        
        # a booking consists of an arrival day, A, and a departure day, D
        #   meaning a stay from day A to day D-1
        # as such a booking consisting of arrival day A and departure day D<=A is a phantom/degenerate booking
        
        arrive.sort()
        depart.sort()
        
        i= 0
        j= 0
        
        current_demand= 0
        # Gotcha, if there is a depart and an arrive on the same day,
        #         current demand should not change
        #  care should be taken in such cases, such that current demand is
        #   decremented and then incremented instead of the other way round,
        #   because incrementing then decrementing may incorrectly trigger
        #   current_demand > K = the number of rooms 
        
        while i < N and j < N:
            if depart[i] <= arrive[j]:
                # {the next event is a departure}
                current_demand-= 1
                i+= 1
            else:
                # {the next event is an arrival}
                current_demand+= 1
                j+= 1
            if current_demand > K:
                return False
        
        # either {all arrivals   have been processed} or
        #        {all departures have been processed}
        
        # if all arrivals   have been processed then True
        # if all departures have been processed, but not all arrivals have been processed,
        #   that means that the set of bookings contains a/some phantom/degenerate bookings
        #   noting that phantom/degenerate bookings have no effect then True
        
        return True
    
    # hotel 0 breaks if there is a departure at day 0
    def hotel0(self, arrive, depart, K):
        
        assert len(arrive) == len(depart)
        
        N= len(arrive)
        
        if N <= K: return True
        
        for i in xrange(N):
            depart[i]*= -1
        
        events= sorted( arrive+depart, key= lambda e : (abs(e), e) )
        
        current_demand= 0
        for i in xrange( 2*N ):
            if events[i] < 0:
                # this event is a departure
                current_demand-= 1
            else:
                # this event is an arrival
                current_demand+= 1
            if current_demand > K:
                return False
        
        return True
    
    def hotel2(self, arrive, depart, K):
        
        assert len(arrive) == len(depart)
        
        N= len(arrive)
        
        if N <= K: return True
        
        earliest_arrival_day= arrive[0]
        
        # O(N)
        for arr in arrive[1:]:
            if arr < earliest_arrival_day:
                earliest_arrival_day= arr
        
        latest_departure_day= depart[0]
        
        # O(N)
        for dep in depart[1:]:
            if dep > latest_departure_day:
                latest_departure_day= dep
        
        # demands[i] wil hold the number of rooms demanded on day i
        demands= [0]*(latest_departure_day - earliest_arrival_day +1)
        
        # worst case O(N * ( max(depart) - min(arrive) -1) )
        for i in xrange(N):
            
            # process the ith booking
            
            arr_day= arrive[i]
            dep_day= depart[i]
            
            for j in xrange(arr_day - earliest_arrival_day, dep_day -earliest_arrival_day):
                demands[j]+= 1
                
                if demands[j] > K:
                    return False
        
        return True