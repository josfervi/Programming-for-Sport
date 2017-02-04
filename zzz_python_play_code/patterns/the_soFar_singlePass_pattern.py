# This is a template for a common pattern.
# I have used this pattern many times.
# For two recent examples of this pattern, check zz_foobar/04-lvl3-2/[my_]solution.py

def findBestResultInOnePass(iterable):
    
    # There must be a total order on the set of possible results,
    # so that we can tell which of two distinct results is better and which is worse
    #
    # For example if the set of possible results were the positive integers up to 200
    # and we were trying to minimize the value of the result,
    # then a result of 10 would be better than a result of 11...
    
    bestResult_soFar = ??? # this must be the value of the worst possible result or if it exists, the value of a known result
                           # for the example discussed, 200 or any value greater than 200 could be used
    
    for item in iterable:
        
        potentiallyBetterResult = getAResultUsingTheInformationFrom(item, other_args)
        
        bestResult_soFar = getBetterResult(bestResult_soFar, potentiallyBetterResult)
    
    bestResult = bestResult_soFar
    
    return bestResult