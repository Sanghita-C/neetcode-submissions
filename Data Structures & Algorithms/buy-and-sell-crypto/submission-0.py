class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        pref_diff = [0]*size
        for i in range(1,size):
            pref_diff[i] = prices[i] - prices[i-1]
        
        maxprofit = 0
        profit = 0 

        for diff  in pref_diff:
            if profit + diff >=0 :
                profit += diff
                maxprofit = max(maxprofit, profit)
            else:
                profit = 0 
        

        return maxprofit

        