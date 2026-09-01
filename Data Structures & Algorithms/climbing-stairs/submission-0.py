class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n= 2
        [- -]--> 1 step or 2 step


        n = 5
        -  1, 4.             2, 3
        -  (1, 3) (2,2).     (1, 2)
        -  (1, 2) (2, 1) (0,)


5 - 4
5-- 3
4- 3
4-2
3-2
3-1
2-1
2-0



3-2
3-1
2-1

        """

        step_ways_mapping = {}

        def count_path(step_number, target):
            nonlocal step_ways_mapping

            if step_number in step_ways_mapping:
                return step_ways_mapping[step_number]
            if step_number == target: 
                return 1
            if step_number > target:
                return 0

                
            step_ways_mapping[step_number] = count_path(step_number +1, target)+count_path(step_number +2, target)

            return step_ways_mapping[step_number]

        
        return count_path(0,n)
             

            



        