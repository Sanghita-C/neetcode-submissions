class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        question: 

        - how big? big enough 
        - can we have array of size 0 or 1? always > 2
        
        algo:

        [1, 2, 3]
            min(2+3,2)    3
            2

        """
        size = len(cost)

        if size ==1:
            return cost[0]

        if size ==2 : 
            return min(cost[0],cost[1])

        min_cost_from_step = [0] * size
        min_cost_from_step[size-1] = cost[size-1]
        min_cost_from_step[size-2] = cost[size-2]
        




        for i in range (size-3,-1,-1):
            
            min_cost_from_step[i] = cost[i]+ min(min_cost_from_step[i+1], min_cost_from_step[i+2] )
            



        return min(min_cost_from_step[0],min_cost_from_step[1])

        