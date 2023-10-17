class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic={}
        for i in ransomNote:
            if dic.has_key(i):
                dic[i] = dic[i]+1
            else:
                dic[i] = 1

        for j in magazine:
            if dic.has_key(j):
                if dic[j] == 1:
                    dic.pop(j)
                else:
                    dic[j] = dic[j]-1
                if dic == {}:
                    return True
        return False
        