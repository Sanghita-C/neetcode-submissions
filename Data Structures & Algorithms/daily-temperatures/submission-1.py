class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [ 30, 38, 30, 36, 35, 40, 28]
        [ ,(36, 3),(40, 5)]

        [1 , 4, 1, 2, 1, 0, 0]


        results [] 
        results[-1] = 0

        loop from end:
            - if next element greater:
                res[i] =. 1
                push to the stack
            - if no
                loop through the stack until u get a greater element
                res[i] = indexfound - i

        """

        size = len(temperatures)

        if size == 1:
            return [0]
        
        res = [0]*size
        stack = []

        for i in range(size -2, -1, -1):
            if temperatures[i+1] > temperatures[i]:
                res[i] = 1
                stack.append([temperatures[i+1], i+1])
            else:
                
                for j in range(len(stack) -1, -1, -1):
                    if stack[j][0] > temperatures[i]:
                        res[i] = stack[j][1] - i
                        break
        
        return res
