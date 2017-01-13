# https://www.interviewbit.com/problems/n3-repeat-number/

# using an extension of the Boyer-Moore Linear Time Majority Vote Algorithm
# http://www.cs.utexas.edu/users/moore/best-ideas/mjrty/index.html

# page 5 of the following paper written by Boyer and Moore offers an insightful analogy
# ftp://net9.cs.utexas.edu/pub/techreports/tr81-32.pdf

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        
        N= len(A)
        if N == 0: return -1
        if N <= 2: return A[0]
        
        first_candidate=  [None, 0]
        second_candidate= [None, 0]
        candidates= [first_candidate, second_candidate]
        
        val= 0
        cnt= 1
        for a in A:
            if   a ==  first_candidate[val]:  first_candidate[cnt]+= 1
            elif a == second_candidate[val]: second_candidate[cnt]+= 1
            elif  first_candidate[cnt] == 0:  first_candidate= [a, 1]
            elif second_candidate[cnt] == 0: second_candidate= [a, 1]
            else:
                first_candidate[cnt]-=  1
                second_candidate[cnt]-= 1
        
        if  first_candidate[cnt] > N/3: return  first_candidate[val]
        if second_candidate[cnt] > N/3: return second_candidate[val]
        
        first_candidate[cnt]=  0
        second_candidate[cnt]= 0
        for a in A:
            if   a ==  first_candidate[val]: first_candidate[cnt]+=  1
            elif a == second_candidate[val]: second_candidate[cnt]+= 1
        
        if  first_candidate[cnt] > N/3: return  first_candidate[val]
        if second_candidate[cnt] > N/3: return second_candidate[val]
        return -1