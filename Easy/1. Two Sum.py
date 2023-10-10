class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if seen.has_key(diff):
                return [seen[diff],i]
            else:
                seen[nums[i]] = i
        return [0]
        