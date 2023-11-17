class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        def recursion(lists):
            ans = [0] * 3
            for i in range(len(lists)):
                idx = i%3
                ans[idx] = max(ans[idx-2]+lists[i],ans[idx-1])
            return max(ans)
        max1 = recursion(nums[:len(nums)-1])
        max2 = recursion(nums[1:])
        return max(max1,max2)