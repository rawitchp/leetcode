class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def recursion(arr,sum_arr,candidates):
            if sum_arr > target:
                return
            elif sum_arr == target:
                ans.append(arr)
                return
            for i in range(len(candidates)):
                new_arr = list(arr)
                new_sum = sum_arr + candidates[i]
                new_arr.append(candidates[i])
                recursion(new_arr,new_sum,candidates[i:])
            return
        recursion([],0,candidates) 
        return ans