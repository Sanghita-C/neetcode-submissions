class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        min_ind = size -1

        for i in range(size -2, 0, -1):
            if nums[i] >= min_ind - i:
                min_ind = i
        
        if nums[0] >= min_ind:
            return True
        
        return False

        