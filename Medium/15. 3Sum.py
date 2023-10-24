class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
                elif(s < 0):
                    j += 1
                else:
                    k -= 1
        return ans

