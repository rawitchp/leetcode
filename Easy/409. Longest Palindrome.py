class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(len(s))
        dic={}
        arr=[]
        ans=0
        have_odd = False
        for i in s:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
                arr.append(i)
        for j in arr:
            if dic[j] % 2 == 0:
                ans += dic[j]
            else:
                ans += dic[j] - 1 
                have_odd = True
        if have_odd:
            return ans + 1
        return ans