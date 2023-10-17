class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        arr = []
        max_num = 't'
        for i in nums:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
            if dic.has_key(max_num) and dic[max_num] < dic[i]:
                max_num = i
            elif max_num == 't':
                max_num = i
        return max_num