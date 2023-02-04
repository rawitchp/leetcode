class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height)-1
        while l < r:
            min_h = min(height[l],height[r])
            area = min_h * (r-l)
            max_area = max(max_area,area)
            if min_h == height[l]:
                l += 1
            else:
                r -= 1
        return max_area