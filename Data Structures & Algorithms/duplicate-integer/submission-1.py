class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Questions:
         - What is the size of the array ? pretty large
         - Can it have 0 elements or just 1 element ? yes
         - Is the array sorted ? No

         Brute force Algo time O(n2), memory: O(1): 
         - For each element in arr:
            - Loop through entire array:
                - Find a match? 
                    - Return False
        - Return True


        Optimization 1 time O(n log n), memory : O(1): 
        - sort the array in ascending order
        - Loop through the sorted array: 
            - if ith element = i-1th element
                return False
        - return True

        Optimization 2 time : O(n), memory: O(n):
        - initiate an empty set
        - Loop through each num in  the array
            - is num in the set?
                - yes - Return False
            - Add the num to the set
        - Return True


        Test Case : 
        [1, 3, 4, 3]
        hashset = [1, 3, 4]

        [1, 3, 4]
        hashset = [1, 3, 4]

        """

        if len(nums) == 0 or len(nums) == 1:
            return False
        
        hashset = set()
        size = len(nums)

        for i in range(size):
            if nums[i] in hashset: 
                return True
            hashset.add(nums[i])
        
        return False


        