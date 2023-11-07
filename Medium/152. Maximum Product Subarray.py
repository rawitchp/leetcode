class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        s = 1
        e = 1
        max_p = 0
        for i,num in enumerate(nums):
            s *= num
            e *= nums[len(nums)-i-1]
            max_cur = max(s,e)
            max_p = max(max_p,max_cur)
            if s == 0:
                s = 1
            if e == 0:
                e = 1
        return max_p