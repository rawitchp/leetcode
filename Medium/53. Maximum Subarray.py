class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -99999
        cur_sum = 0
        for i in nums:
            cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum <= 0:
                cur_sum = 0
        return max_sum