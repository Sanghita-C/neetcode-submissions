class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums = [ 2,20,4,10,3,4,5]

        2,3,4,4,5,10,11,20

    c.  1 2 3 3 4 1 2 1
    ml  1 2 3 3 4 4 4 4

        ans = [2,3,4,5]

        nums = [4, 2, 3, 1]

        set = [1,2,3,4]

        ans = 1,2,3,4
        """

        existing_num = set()

        for i in range(len(nums)):
            existing_num.add(nums[i])
        
        count = 0
        maxlen = 0

        for i in range(len(nums)):
            if nums[i] - 1 in existing_num:
                continue
            j = nums[i]
            count =0
            while j in existing_num:
                count +=1
                j += 1
            maxlen = max(count,maxlen)
        
        return maxlen



      
