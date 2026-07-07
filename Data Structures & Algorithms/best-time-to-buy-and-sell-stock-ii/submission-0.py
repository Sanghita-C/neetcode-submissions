class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices                [7, 1,  5,  3,  6,  4]
    
    consecutive_transaction = [0, -6, 4,  -2,  3, -2]



        -7 + 3 = -4 = (-7 +1) + (-1 +5) + (-5 +3) = -6 + 4 + -2 = -4

        - consecutive_trans =  store price[i] - price[i-1]
        - maxprofit = 0, curent_prof = 0

        - loop through consec_trans: 
            curr_profit += consec_trans[i]
            if curr_profit < 0 : 
                reset to 0
            max_profit = max(max_profit, curr prfut)

        return max profit

        """

        size = len(prices)
        consecutive_transactions = [0]* size

        for i in range(1,size):
            consecutive_transactions[i]=  prices[i] - prices[i-1]
        
        max_profit = 0 
        curr_profit = 0
        total_profit = 0

        for i in range(size):
            total_profit += consecutive_transactions[i] if consecutive_transactions[i] >0 else 0
        
        return total_profit




        