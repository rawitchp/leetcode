class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(intervals)
        for i in range(n):
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = intervals[i]
            elif intervals[i][1] >= newInterval[0] or intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        ans.append(newInterval) 
        return ans