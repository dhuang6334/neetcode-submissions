"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start = sorted(start)
        end = sorted(end)

        count = 0
        i = 0
        j = 0
        maxCount = 0
        print(start)
        print(end)
        while i < len(start) or j < len(end):
            if (i < len(start) and start[i] < end[j]):
                count += 1
                maxCount = max(maxCount, count)
                i += 1
            else:# (start[i] > end[j]):
                count -= 1
                j += 1
            print(count)
        return maxCount
            