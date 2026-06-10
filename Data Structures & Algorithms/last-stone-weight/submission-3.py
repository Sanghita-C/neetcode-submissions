class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >=2:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            if stone2-stone1 !=0 :
                heapq.heappush(stones,-abs(stone2-stone1))
            
        if len(stones) == 0:
            return 0
        else:
             return -1* heapq.heappop(stones)

        