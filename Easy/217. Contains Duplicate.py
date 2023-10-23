class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        for i in nums:
            if dic.has_key(i):
                return True
            else:
                dic[i] = 1
        return False