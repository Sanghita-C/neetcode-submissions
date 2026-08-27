class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Questions: 
        - len of array : huge
        - always having an answer? yes
        - sorted? No
        - len 0 ? always greater than 2
        - i and j is different

        Algorithm 1 Time: O(N2), mem : O(1): 
        - sin, lin
        - loop sin from 0 to len arr
            - loop lin from sin+1 to len arr
                - if sin + lin == target:
                    return [sin, lin]
        
        Algorithm 2 Time: O(N) , mem O(N): 
        - index_map = {}
        - for each num in arr:
            check if target - num exists as key
                - yes, return [ index of target-num, index of num]
            add to index map - num, index
            increase index

        

        """

        index_map = {}
        size = len(nums)
        index = 0

        for num in nums: 
            if target - num in index_map:
                return [index_map[target - num], index]

            index_map[num] = index
            index += 1
        
        return []


        