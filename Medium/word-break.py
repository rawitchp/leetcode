class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        myset = set(wordDict)
        flag = [-1]*(len(s)+1)
        def check(s):
            if len(s) == 0:
                return True
            if flag[len(s)] != -1:
                return flag[len(s)]
            for i in range(len(s)+1):
                sub = s[:i]
                for j in myset:
                    if sub == j:
                        ans = check(s[i:])
                        if ans:
                            flag[len(sub)] = 1
                            return True
            flag[len(s)] = 0
            return False
        return check(s)