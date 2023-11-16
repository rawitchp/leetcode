class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        idx = 0
        ans = 0
        while idx < len(nums)-1:
            ans += 1
            next_idx = idx+1
            for i in range(1,nums[idx]+1):
                if idx + i >= len(nums)-1:
                    return ans
                if nums[next_idx]+ next_idx <= nums[i+idx] + i + idx:
                    next_idx = i + idx
            idx = next_idx
        return ans