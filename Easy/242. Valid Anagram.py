class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            if dic1.has_key(s[i]):
                dic1[s[i]] += 1
            else:
                dic1[s[i]] = 0
            if dic2.has_key(t[i]):
                dic2[t[i]] += 1
            else:
                dic2[t[i]] = 0
        return dic1 == dic2
        