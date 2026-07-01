class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [1,2,3,0,2]

        maxp = [2,-1,2,0]

        3 -> max(-3,-1) = -1
        2-> max(1,2)


        [5, 4, 6, 2, 8]
        """

        if len(prices)==1 or len(prices) == 0:
            return 0

        size = len(prices)
        max_profit_ith_day = [0] * size
        max_profit_ith_day[size -2 ] = max(0,prices[size-1] - prices[size-2])
        

        for i in range(size-3,-1,-1):
            maxprofit = 0
            for j in range(i,size):
                profit = prices[j] - prices[i]
                if i==j:
                    profit += max_profit_ith_day[j+1]
                elif j+2 <size:
                    profit += max_profit_ith_day[j+2]
                maxprofit = max(profit,maxprofit)
                
            max_profit_ith_day[i] = maxprofit

        return max_profit_ith_day[0]
    
        