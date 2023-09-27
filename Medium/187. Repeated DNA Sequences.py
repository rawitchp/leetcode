
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """"
        :type s: str
        :rtype: List[str]
        """
        start = 0
        sub = {}
        ans = []
        while start + 9 < len(s):
            string = s[start:start+10]
            if(string in sub and sub[string] == 1):
                sub[string] = 2
                ans.append(string)
            elif(string not in sub):
                sub[string] = 1
            start += 1
        return ans