class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        [1, 7, 2, 5, 4, 7, 3, 6]

        1 -> 1*(7-0) = 7 == maxvol 
            height 1 - already max

        7 -> 6 * (6) = 36  : 7* 5 =35 < 36



        height of water being held <= height[i]
        last occurrence where we have a wall >= height[i]

        for each pillar : 
            max out the width and find the corresponding volume
            if the last pillar height < present pillar: 
                - max height could only be the height of pillar itself
                - we need to see the width pointer
                - check the index at which present height * width > present volume
                - if we find that index - start moving from that index to the right and find if there is a height >= present height 


        """

        start = 0
        end = len(heights) - 1

        maxvolume = 0 

        while start < end:
            width = end - start
            height = min (heights[start], heights[end])
            currvol = height * width 
            maxvolume = max(maxvolume, currvol)

            
            if heights[start] <= heights[end]:
                start +=1
            else:
                end -=1 
        
        return maxvolume
                
        