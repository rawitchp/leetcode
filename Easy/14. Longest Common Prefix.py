class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        f = strs[0]
        for i in range(len(f)):
            for w in strs[1:]:
                if i == len(w) or w[i] != f[i] :
                    return f[:i]
        return f