class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        graph = [[] for i in range(numCourses)]
        q = []
        print(graph)
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        visited = 0
        while q:
            node = q.pop(0)
            visited += 1
            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return visited == numCourses