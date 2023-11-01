class Solution:
    def rob(self, nums: List[int]) -> int:
        s = [0] * len(nums)
        i = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        while i > -1:
            if i == len(nums) - 1 or i == len(nums) - 2:
                s[i] = nums[i]
            elif i == len(nums) - 3:
                s[i] = nums[i] + s[i+2]
            else:
                s[i] = max(nums[i]+s[i+2],nums[i]+s[i+3])
            i -= 1
        return max(s[0],s[1])