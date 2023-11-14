class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        prev = "#"
        max_count = 1
        count = 1
        for i in nums:
            if prev == "#":
                prev = i
                count = 1
            elif i == prev+1:
                count += 1
                prev = i
            elif i == prev:
                continue
            else:
                prev = i
                max_count = max(count,max_count)
                count = 1
        return max(max_count,count)