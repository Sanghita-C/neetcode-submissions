class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_num_map = {}
        i = 0
        for num in nums: 
            if target - num in index_num_map.keys():
                return [index_num_map[target - num],i]
            index_num_map[num] = i 
            i += 1
        return [0,0]




        
        