class Solution(object):
    def merge(self, intervals):
        ans = []
        intervals.sort()

        if len(intervals) == 0:
            return ans

        temp = intervals[0]
        for interval in intervals:
            if interval[0] <= temp[1]:
                temp[1] = max(temp[1], interval[1])
            else:
                ans.append(temp)
                temp = interval
        ans.append(temp)

        return ans