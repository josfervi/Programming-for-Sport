# https://www.interviewbit.com/problems/fizzbuzz/# https://www.interviewbit.com/problems/fizzbuzz/

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, N):
        
        nums = [None]*N
        
        for num in range(1,N+1):
            
            i = num-1
            
            if num % 15 == 0:
                nums[i] = 'FizzBuzz'
            elif num % 3 == 0:
                nums[i] = 'Fizz'
            elif num % 5 == 0:
                nums[i] = 'Buzz'
            else:
                nums[i] = num
        
        return nums
