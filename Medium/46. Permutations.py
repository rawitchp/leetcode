class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def recursion(nums,p_list):
            if not nums:
                ans.append(p_list)
                return
            for i in range(len(nums)):
                new_p = list(p_list)
                new_nums = list(nums)
                new_p.append(nums[i])
                new_nums.pop(i)
                recursion(new_nums,new_p)

        recursion(nums,[])
        return ans