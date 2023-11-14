class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = '#' + "#".join(s) + '#'
        center = right = 0
        lists = [0] * len(s)
        ans = s[0]
        for i in range(len(s)):
            if i <= right:
                lists[i] = min(right-i,lists[2*center-i])
            while i-lists[i]-1 >=0 and i+lists[i]+1 < len(s) and s[i-lists[i]-1] == s[i+lists[i]+1]:
                lists[i] += 1
            if i + lists[i] > right:
                center = i
                right = i + lists[i]
            if lists[i]*2 + 1 > len(ans):
                center = i
                right = i + lists[i]
                ans = s[i-lists[i]:i+lists[i]+1]
        ans = ans.replace('#','')

        return ans