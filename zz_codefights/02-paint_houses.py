def paintHouses(cost):
    
    if not cost:
        return 0
    
    n = len(cost)
    
    R, B, G = 0, 1, 2
    
    dp = (0, 0, 0)
    
    # INVARIANT:
    #   at the beginning of the loop, dp contains
    #   (
    #     min total cost to paint the first i houses (0 to i-1), given we paint house i-1 RED
    #     min total cost to paint the first i houses (0 to i-1), given we paint house i-1 BLUE
    #     min total cost to paint the first i houses (0 to i-1), given we paint house i-1 GREEN
    #   )
    for house in cost:
        
        dp = ( min(dp[B], dp[G]) + house[R],
               min(dp[R], dp[G]) + house[B],
               min(dp[R], dp[B]) + house[G] )
    
    return min(dp)


def paintHouses_linearSpace(cost):
    
    n = len(cost)
    
    R = 0
    B = 1
    G = 2
    
    min_tot_cost_R = [None]*n
    min_tot_cost_R[0] = cost[0][R]
    
    min_tot_cost_B = [None]*n
    min_tot_cost_B[0] = cost[0][B]
    
    min_tot_cost_G = [None]*n
    min_tot_cost_G[0] = cost[0][G]
    
    for i in range(1, n):
        
        min_tot_cost_R[i] = min(min_tot_cost_B[i-1], min_tot_cost_G[i-1]) + cost[i][R]
        
        min_tot_cost_B[i] = min(min_tot_cost_R[i-1], min_tot_cost_G[i-1]) + cost[i][B]
        
        min_tot_cost_G[i] = min(min_tot_cost_R[i-1], min_tot_cost_B[i-1]) + cost[i][G]
    
    min_tot_cost = min( min_tot_cost_R[-1], min_tot_cost_B[-1], min_tot_cost_G[-1] )
    
    return min_tot_cost