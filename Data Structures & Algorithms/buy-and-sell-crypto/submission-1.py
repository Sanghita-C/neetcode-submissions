class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [] - ith day value of a stock

        Questions: 

        - How large is the array : pretty large
        - 1 enlisted day ? yes
        - the prices will be > 0

        [ 10, 1, 5, 6, 7, 1]

        buy_price: 1  sell_price: 1 profit: 6

        Algorithm: 

        buy_price - initiate it with first day
        max_profit = 0
        iterate the rest of the days:
            if price at day i is < buy_price:
                buy_price = present day price
            profit = price_ith_day - buy_price
            max_profit = max(profit, max_profit)

        """

        buy_price = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[i] <buy_price:
                buy_price = prices[i]
            else:
                profit = prices[i]  - buy_price
                max_profit = max(profit, max_profit)
            
        return max_profit
