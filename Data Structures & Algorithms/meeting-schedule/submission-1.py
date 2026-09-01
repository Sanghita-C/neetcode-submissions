"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        overlapping - the boundary can be same instant

        algo: 
        - sort it in start time


        [(5,8), (9,10)]

        [ (1,10), (5,8)]

        """
        size = len(intervals) 
        if size ==0 or size ==1:
            return True

        intervals.sort(key= lambda x: x.start)

        for i in range(1,size):
            if intervals[i].start <intervals[i-1].end:
                return False
        
        return True

