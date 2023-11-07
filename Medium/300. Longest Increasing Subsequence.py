class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                l = 0
                r = len(ans)-1
                mid = 0
                while l <= r:
                    mid = (l+r)//2
                    if (ans[mid] > nums[i] and ans[mid-1] < nums[i]) or ans[mid] == nums[i]:
                        break
                    elif nums[i] < ans[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                ans[mid] = nums[i]
        return len(ans)