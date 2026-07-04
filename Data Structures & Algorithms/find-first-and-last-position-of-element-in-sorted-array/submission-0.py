class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        if target found = [l,r]
        if target not found = [-1, -1]
        low_index = len + 1
        high_index = -1
        start =0 , end = l -1
        mid = start+end//2
        if mid == target: 
            low = min(low, mid)
            high = max(high, mid)
            search left side
            search right side
        if mid < taget:
            search left side
        if mid> target: 
            search righ side
        """

        size = len(nums)
        low_index = size
        high_index = -1
        start = 0
        end = size -1

        def binary_search( nums, target,start, end):
            nonlocal low_index, high_index

            if start > end:
                return


            mid = int((start + end)/2 )

            if nums[mid] == target:
                low_index = min(low_index,mid)
                high_index = max(high_index, mid)
                #print(f"Match found: setting low_index to {low_index} and high_index to {high_index}.")
                binary_search(nums,target, mid+1,end)
                binary_search(nums,target, start,mid-1)

            elif nums[mid] < target:
                binary_search(nums,target,mid+1,end)
            else:
                binary_search(nums,target,start,mid-1)

        binary_search(nums,target,start,end)
        if low_index == size:
            return [-1,-1]
        
        return [low_index,high_index]


