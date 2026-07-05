class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        """
        arr =        [  1, 1, 1]
        pref_arr =    [. 1, 2, 3]
        suff_arr=.    [.  3, 2, 1]

        [ x1,  x2, x3, x4, x5, x6, x7]

        target = total - suffix[x7] - pref[x5]

        pref[x4] + suff[x7] = total - target = goal
        pref[x4 ] - pref[x6] = -target
        pref[x6] - pref[x4] = target
        pref[x4] = pref[x6] - target

        index(x6) > index(x4)

        """

        pref_sum_freq = {0: 1}
        prefix_sum = 0
        total_count = 0

        for num in nums:
            prefix_sum += num

            total_count += pref_sum_freq.get(prefix_sum - k, 0)

            pref_sum_freq[prefix_sum] = pref_sum_freq.get(prefix_sum, 0) + 1

        return total_count







        