class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        can we have less than two stones at present ? yes

        Algo: 

        - create a maxheap out of the list
        - get the two highest weights
        - perform calculation
        - if needed add new element
        """

        stones_heap = [ -weight for weight in stones]
        heapq.heapify(stones_heap)

        while len(stones_heap) > 1:
            first = - (heapq.heappop(stones_heap))
            second = -(heapq.heappop(stones_heap))

            if first > second:
                new_weight = -(first - second)
                heapq.heappush(stones_heap, new_weight)
            
        
        if len(stones_heap) ==0:
            return 0
        
        return -1* stones_heap[0]
        