class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1 or len(prices) == 0:
            return 0

        size = len(prices)
        max_profit_ith_day = [0] * size
        best_sell_profit = prices[size-1]
        

        for i in range(size-2,-1,-1):
            cool_down_profit = 0 + max_profit_ith_day[i+1]
            sell_day_profit = -prices[i] + best_sell_profit
            max_profit_ith_day[i] = max(cool_down_profit, sell_day_profit)
            if i<size-2:
                best_sell_profit = max(best_sell_profit, prices[i] + max_profit_ith_day[i+2])
            else:
                best_sell_profit = max(best_sell_profit, prices[i])

        return max_profit_ith_day[0]