from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = [0] * numCourses
        lists = defaultdict(list)
        for i in prerequisites:
            degrees[i[0]] += 1
            lists[i[1]].append(i[0])
        q = []
        ans = []
        for i,degree in enumerate(degrees):
            if degree == 0:
                q.append(i)
        while q:
            s = q.pop(0)
            ans.append(s)
            for i in lists[s]:
                degrees[i] -= 1
                if degrees[i] == 0:
                    q.append(i)
        if len(ans) != numCourses:
            return []
        return ans