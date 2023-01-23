class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            present_char = strs[0][i]
            # print(present_char)
            similar = True
            for j in range(len(strs)-1):
                if(i >= len(strs[j+1])):
                    similar = False
                    break
                if(present_char != strs[j+1][i]):
                    similar = False
            # print(similar)
            if(not similar):
                break
            prefix += present_char
            # print(prefix)
        return prefix