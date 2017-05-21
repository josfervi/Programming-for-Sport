# https://www.interviewbit.com/problems/stocks2/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    # [10, 7, 5, 8, 11, 9] 
    def maxProfit(self, stock_prices):
        
        if not stock_prices:
            return 0
        
        sum_ = 0
        prev_price = stock_prices[0]
        for price in stock_prices[1:]:
            
            sum_ += max(0, price - prev_price)
            prev_price = price
            
        return sum_
