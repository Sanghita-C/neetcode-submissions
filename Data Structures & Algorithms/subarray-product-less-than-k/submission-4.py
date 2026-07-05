class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        [x1, x2, x3, x4, x6, x7, x8]
                             i 
                  j
        
        """

        min_in = 0
        curr_in = 0
        count = 0
        size = len(nums)
        pref_prod = 1

        for num in nums:
            pref_prod = num * pref_prod
            if pref_prod >= k:
                while min_in <= curr_in and pref_prod >=k:
                    pref_prod = int(pref_prod / nums[min_in])
                    min_in +=1

            count += max(curr_in - min_in  + 1,0)
            curr_in +=1

        return count



