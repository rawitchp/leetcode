class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        first = 0
        longest = 0
        cur_long = 0
        for i in range(len(s)):
            if dic.has_key(s[i]):
                if dic[s[i]] >= first:
                    first = dic[s[i]]+1
                    dic[s[i]] = i
                    cur_long = i - first + 1
                else:
                    dic[s[i]] = i
                    cur_long += 1
            else:
                dic[s[i]] = i
                cur_long += 1
            longest = max(longest,cur_long)
        return longest