class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        ans = [1] * l
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        right = nums[l-1]
        for i in range(l-2,-1,-1):
            ans[i] *= right
            right *= nums[i]
        return ans