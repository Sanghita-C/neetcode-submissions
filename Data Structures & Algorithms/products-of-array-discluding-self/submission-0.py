class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        preprd = [0]* size
        pstprd = [0]* size

        preprd[0] = nums[0]
        pstprd[size-1] = nums[size -1]

        for i in range(1,size):
            preprd[i] = preprd[i-1]*nums[i]

        for i in range(size - 2,-1,-1):
            pstprd[i] = pstprd[i+1]*nums[i]
        
        print(preprd)
        print(pstprd)

        output = [0]*size

        for i in range(size):
            if i == 0:
                output[i] = pstprd[i+1]
            elif i == size -1: 
                output[i] = preprd[i-1]
            else:
                output[i] = preprd[i-1] * pstprd[i+1]

        return output
        


        