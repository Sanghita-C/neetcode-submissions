class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            [1,4] [2, 8] [3,4], 
            [1,8]



            Thoughts and cases : 
            - start time is increasing
            - i+1 start > i_end - non overlapping
            - i+1 start = i_end -- overlapping
            - i+1 start < i_end -- overlapping
        """
        size = len(intervals)
        sorted_intervals = sorted(intervals, key = lambda item :item[0] )
        print(sorted_intervals)
        time_stack = []
        time_stack.append(sorted_intervals[0])

        for i in range(1,size):
            start = sorted_intervals[i][0]
            end = sorted_intervals[i][1]

            prev_time= time_stack[-1]
            #time_stack.pop()
            
            if start > prev_time[1]:
                time_stack.append([start,end])
            elif start == prev_time[1]:
                prev_time[1] = end
                time_stack.pop()
                time_stack.append(prev_time)
            else:
                prev_time[1] = end if prev_time[1] < end else prev_time[1]
                time_stack.pop()
                time_stack.append(prev_time)
                

        return time_stack