class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        presum = 0
        dict = {0:1}
        for i in nums:
            presum += i
            if (presum-k) in dict:
                res = res + dict[presum-k]
            if presum not in dict:
                dict[presum] = 1
            else:
                dict[presum] = dict[presum]+1
        return res