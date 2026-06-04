from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for start, end, price in flights:
            graph[start].append((end, price))

        INF = 10**9
        memo = [[-1] * (k + 2) for _ in range(n)]

        def dfs(node, steps):
            if node == dst:
                return 0

            if steps == k + 1:
                return INF

            if memo[node][steps] != -1:
                return memo[node][steps]

            ans = INF

            for nei, price in graph[node]:
                ans = min(ans, price + dfs(nei, steps + 1))

            memo[node][steps] = ans
            return ans

        result = dfs(src, 0)

        return -1 if result >= INF else result