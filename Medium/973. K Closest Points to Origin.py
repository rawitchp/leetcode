class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr_dis = []
        count = 0
        for i,j in points:
            pair = [pow(i,2)+pow(j,2),count]
            arr_dis.append(pair)
            count += 1
        arr_dis = sorted(arr_dis)
        ans = []
        for i in range(k):
            ans.append(points[arr_dis[i][1]])
        return ans