class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        f = nums[0]
        nums.sort()
        idx = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == f:
                idx = mid
                break
            elif nums[mid] > f:
                r = mid - 1
            else:
                l = mid + 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2 
            if nums[mid] == target:
                if mid < idx:
                    return abs(mid + len(nums) - idx) 
                else:
                    return mid-idx
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1