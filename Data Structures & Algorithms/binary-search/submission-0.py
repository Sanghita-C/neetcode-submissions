class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        question: 

        length array? huge
        can we have empty array cases - no 
        can target be less than or greater than the numbers min , max of numbers in the list - possible



        distinct 
                [-1, 0, 2, 4, 6, 8]
    low =   0. 3  3
    high=   5  5. 3
    mid =  2.  4.  3


        """

        if target < nums[0]:
            return -1
        if target > nums[-1]:
            return -1
        
        low =0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) //2

            print ("Mid point index being checked for is: ",mid)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low= mid +1
            
            else:
                high = mid -1
        

        return -1
            

        