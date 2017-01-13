def merge_ranges(ranges):
    
    N= len(ranges)
    
    if N < 2:
        return ranges
    
    i= 1
    while i < len(ranges): # use len(ranges) instead of N because length of ranges IS changing 
        if overlap( ranges[i-1], ranges[i] ):
            # merge them
            new_lower_bound= ranges[i-1].lower_bound
            new_upper_bound= max( ranges[i-1].upper_bound, ranges[i].upper_bound )
            ranges[i-1]= Range(new_lower_bound, new_upper_bound)
            del ranges[i]
            i-= 1
        i+= 1
    
    return ranges

def overlap( earlier_range, later_range ):
    return earlier_range.upper_bound >= later_range.lower_bound